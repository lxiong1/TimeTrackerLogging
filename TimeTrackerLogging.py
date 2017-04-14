import time
import json
import keyring
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#time the hour logging
start_time = time.time()

print("Weekly Logging Script Running, Please Wait For Further Instructions...")

with open("C:/Users/luexi/Desktop/TimeTrackerLogging/eBillityUserProfiles.json") as json_data:
    employee_data = json.load(json_data)

desktop_executor = "http://127.0.0.1:4444/wd/hub/"
desired_caps_values = {"browserName" : "phantomjs",
                       "platform" : "WINDOWS",
                       "javascriptEnabled" : True,
                       "cssSelectorsEnabled" : True,
                       "phantomjs.binary.path" : "C:/Users/luexi/AppData/Roaming/npm/node_modules/phantomjs-prebuilt/lib/phantom/bin/phantomjs.exe"
                       }

driver = webdriver.Remote(
    command_executor = desktop_executor,
    desired_capabilities = desired_caps_values
)

wait = WebDriverWait(driver, 10)

#necessary to set dummy window size for finding elements even though it is headless browser
driver.set_window_size(1120, 550)
driver.get("https://ebillity.com")
# driver.maximize_window()

#login credentials
email = employee_data["Lue Xiong"]["email"]
keyring.set_password("system", "username", "password")

#click login toggle button
login_toggle = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'loginToggle')))
login_toggle.click()

login_email_field = wait.until(EC.element_to_be_clickable((By.ID, "emailAddress")))
login_email_field.click()
login_email_field.send_keys(email + Keys.TAB + keyring.get_password("system", "password") + Keys.RETURN)

close_pop_up = wait.until(EC.element_to_be_clickable((By.ID, "ctl00_ContentPlaceHolder1_imagClose")))
close_pop_up.click()

entries_tab = wait.until(EC.element_to_be_clickable((By.ID, "ctl00_menubar_EntriesNavLabel")))
entries_tab.click()

#initiate question for user input to trigger the if statements
print("y = Yes " + "n = No " + "lw = Last Week (Use This Input If You Forgot To Log Your Hours For Last Week)")
normal_week_response = input("Did You Work The Normal 8 Hours A Day For The Week? (y/n/lw): ")

def get_iterated_log_box():
    hour_log_box_weekdays = driver.find_elements_by_css_selector("div.day input")[0:5]
    return hour_log_box_weekdays

def get_client():
    client = employee_data["Lue Xiong"]["client"]
    return client

def get_client_two():
    client_two = employee_data["Lue Xiong"]["client_two"]
    return client_two

def get_timesheet_user_profile(c):
    #Any client containing string "Unbillable" will uncheck the billable checkbox
    if "Unbillable" in c():
        billable_checkbox = driver.find_element_by_css_selector(".bill input")
        billable_checkbox.click()

    time.sleep(0.75)
    customer_dropdown = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".w-row-qbo .select2-container.combo-weekly .select2-chosen")))
    customer_dropdown.click()
    customer_dropdown_search_field = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#select2-drop .select2-search .select2-input")))
    customer_dropdown_search_field.send_keys(c())
    time.sleep(0.75)
    customer_dropdown_search_field.send_keys(Keys.RETURN)

    time.sleep(0.75)
    service_item_dropdown = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".w-row-qbo .activity .select2-container.combo-weekly .select2-chosen")))
    service_item_dropdown.click()
    service_item_dropdown_search_field = wait.until(EC.visibility_of_any_elements_located((By.CSS_SELECTOR, "#select2-drop .select2-search .select2-input")))[0]
    service_item_dropdown_search_field.send_keys(c())
    time.sleep(0.75)
    service_item_dropdown_search_field.send_keys(Keys.RETURN)

# def check_for_client_two(ct):
#     ct()
#
#     #Check for existing second client
#     for check in ct():
#         if check != None:
#             hour_log_box_weekdays_two = driver.find_elements_by_css_selector("div.day input")[5:10]
#         elif check == None:
#             pass

def wait_for_save_successful():
    wait.until(EC.text_to_be_present_in_element((By.ID, "ctl00_ResultLabel"), "Saved successfully"))

def make_a_comment():
    comment = input("Would You Like To Leave A Comment For Your Logged Hours? If Not Leave This Blank: ")
    if comment != "":
        description_box = driver.find_element_by_css_selector(".w-row-qbo .desc textarea")
        description_box.clear()
        #Keys.TAB is used to get out of comment box to persist comment
        description_box.send_keys(comment + Keys.TAB)
        print("Your Comment Has Been Registered")
        time.sleep(1)
        driver.quit()
    elif comment == "":
        driver.quit()

def y_response(log_box):
    print("Logging Your Normal Weekly Hours Now...")
    get_timesheet_user_profile(get_client)
    logHour = "8"
    log_box()
    for day in log_box():
        day.clear()
        day.send_keys(logHour)
        day.send_keys(Keys.TAB)
        wait_for_save_successful()

def n_response(log_box):
    get_timesheet_user_profile(get_client)

    print("Please Specify Your Hours For This Week")
    specified_monday_hours_input = input("Enter Your Hours For Monday: ")
    specified_tuesday_hours_input = input("Enter Your Hours For Tuesday: ")
    specified_wednesday_hours_input = input("Enter Your Hours For Wednesday: ")
    specified_thursday_hours_input = input("Enter Your Hours For Thursday: ")
    specified_friday_hours_input = input("Enter Your Hours For Friday: ")

    log_box()

    print("Logging Your Specified Hours Now...")
    log_box()[0].clear()
    log_box()[0].send_keys(specified_monday_hours_input)
    log_box()[0].send_keys(Keys.TAB)

    wait_for_save_successful()
    log_box()[1].clear()
    log_box()[1].send_keys(specified_tuesday_hours_input)
    log_box()[1].send_keys(Keys.TAB)

    wait_for_save_successful()
    log_box()[2].clear()
    log_box()[2].send_keys(specified_wednesday_hours_input)
    log_box()[2].send_keys(Keys.TAB)

    wait_for_save_successful()
    log_box()[3].clear()
    log_box()[3].send_keys(specified_thursday_hours_input)
    log_box()[3].send_keys(Keys.TAB)

    wait_for_save_successful()
    log_box()[4].clear()
    log_box()[4].send_keys(specified_friday_hours_input)
    log_box()[4].send_keys(Keys.TAB)

def lw_response():
    last_week_response = input("Did You Forget To Log Your Hours For Last Week? (y/n): ")
    if last_week_response == "y":
        date_dropdown = wait.until(EC.visibility_of_element_located((By.ID, "ddlDateRange")))
        date_dropdown.click()
        date_dropdown.send_keys(Keys.ARROW_UP + Keys.RETURN)
        normal_last_week_response = input("Did You Work The Normal 8 Hours A Day For Last Week? (y/n): ")
        if normal_last_week_response == "y":
            y_response(get_iterated_log_box)
        elif normal_last_week_response == "n":
            n_response(get_iterated_log_box)
    elif last_week_response == "n":
        normal_week_response = input("Did You Work The Normal 8 Hours A Day For This Week? (y/n/lw): ")
        if normal_week_response == "y":
            y_response(get_iterated_log_box)
        elif normal_week_response == "n":
            n_response(get_iterated_log_box)
        elif normal_week_response == "lw":
            lw_response()

#if yes, sends 8 hours each for Monday-Friday; lwwise specify hours
if normal_week_response == "y":
    y_response(get_iterated_log_box)
elif normal_week_response == "n":
    n_response(get_iterated_log_box)
elif normal_week_response == "lw":
    lw_response()

# submit_weekly_timesheet = wait.until(EC.element_to_be_clickable((By.ID, "btnSubmit")))
# submit_weekly_timesheet.click()

print("Logging Hours Finished In", time.time() - start_time, "Seconds")
make_a_comment()