import time
import json
import getpass
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

with open("../../Desktop/time_tracker_log/eBillityUserProfiles.json") as json_data:
    employee_data = json.load(json_data)

your_name = input("Hello, What Is Your First and Last Name?: ").title().strip()
if your_name not in employee_data:
    print("Name Is Invalid, Please Enter Valid Name...")
    your_name = input("What Is Your First and Last Name?: ").title().strip()
elif your_name in employee_data:
    print("Okay {}, Pulling Your Profile... Please Wait For Further Instructions As Script Is Now Running".format(your_name))

desktop_executor = "http://127.0.0.1:4444/wd/hub/"

driver = webdriver.Remote(
    command_executor = desktop_executor,
    desired_capabilities = DesiredCapabilities.CHROME
)

wait = WebDriverWait(driver, 10)

driver.get("https://ebillity.com")
driver.maximize_window()

email = employee_data[your_name]["email"]
password = getpass.getpass()

login_toggle = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'loginToggle')))
login_toggle.click()

login_email_field = wait.until(EC.element_to_be_clickable((By.ID, "emailAddress")))
login_email_field.click()
login_email_field.send_keys(email + Keys.TAB + password + Keys.RETURN)

close_pop_up = wait.until(EC.element_to_be_clickable((By.ID, "ctl00_ContentPlaceHolder1_imagClose")))
close_pop_up.click()

entries_tab = wait.until(EC.element_to_be_clickable((By.ID, "ctl00_menubar_EntriesNavLabel")))
entries_tab.click()

auto_save_off = wait.until(EC.element_to_be_clickable((By.ID, "rblAutoSave_1")))
if auto_save_off.is_selected():
    pass
else:
    auto_save_off.click()

client = employee_data[your_name]["client"]
client_two = employee_data[your_name]["client_two"]
client_three = employee_data[your_name]["client_three"]

def get_client():
    client = employee_data[your_name]["client"]
    return client

def get_client_two():
    client_two = employee_data[your_name]["client_two"]
    return client_two

def get_client_three():
    client_three = employee_data[your_name]["client_three"]
    return client_three

def get_iterated_log_box():
    hour_log_box_weekdays = driver.find_elements_by_css_selector("div.day input")[0:5]
    return hour_log_box_weekdays

def get_iterated_log_box_two():
    hour_log_box_weekdays = driver.find_elements_by_css_selector("div.day input")[7:12]
    return hour_log_box_weekdays

def get_iterated_log_box_three():
    hour_log_box_weekdays = driver.find_elements_by_css_selector("div.day input")[14:19]
    return hour_log_box_weekdays

def billable_checkbox(c):
    billable_checkbox_uncheck = driver.find_elements_by_css_selector(".w-row .bill input")[0:5]

    # Any client containing string "Unbillable" will uncheck the billable checkbox
    if "Unbillable" in c():
        if c == get_client:
            billable_checkbox_uncheck[0].click()
        elif c == get_client_two:
            billable_checkbox_uncheck[2].click()
        elif c == get_client_three:
            billable_checkbox_uncheck[4].click()

def make_a_comment(c):
    comment = input("Would You Like To Leave A Comment For Your Logged Hours? If Not, Leave This Blank: ").strip()
    description_box = driver.find_elements_by_css_selector(".w-row-qbo .desc textarea")[0:3]

    if comment != "":
        if c == get_client:
            description_box[0].clear()
            description_box[0].send_keys(comment + Keys.TAB)
        elif c == get_client_two:
            description_box[1].clear()
            description_box[1].send_keys(comment + Keys.TAB)
        elif c == get_client_three:
            description_box[2].clear()
            description_box[2].send_keys(comment + Keys.TAB)
        print("Your Comment Has Been Registered")
    if comment == "":
        pass

def save_submit_quit():
    save_button = driver.find_element_by_id("btnSave")
    save_button.click()

    submit_weekly_timesheet = wait.until(EC.element_to_be_clickable((By.ID, "btnSubmit")))
    submit_weekly_timesheet.click()
    print("Logging Hours Finished")

    driver.quit()
    raise SystemExit

def get_timesheet_user_profile(c):
    customer_dropdown = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".w-row-qbo .select2-container.combo-weekly .select2-chosen")))
    time.sleep(0.5)
    customer_dropdown.click()
    customer_dropdown_search_field = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#select2-drop .select2-search .select2-input")))
    customer_dropdown_search_field.send_keys(c())
    time.sleep(1.5)
    customer_dropdown_search_field.send_keys(Keys.RETURN)

    service_item_dropdown = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".w-row-qbo .activity .select2-container.combo-weekly .select2-chosen")))
    time.sleep(0.5)
    service_item_dropdown.click()
    service_item_dropdown_search_field = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#select2-drop .select2-search .select2-input")))[0]
    service_item_dropdown_search_field.send_keys(c())
    time.sleep(1.5)
    service_item_dropdown_search_field.send_keys(Keys.RETURN)

def get_timesheet_user_profile_two(c):
    customer_dropdown = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".w-row-qbo .select2-container.combo-weekly .select2-chosen")))[2]
    time.sleep(0.5)
    customer_dropdown.click()
    customer_dropdown_search_field = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#select2-drop .select2-search .select2-input")))
    customer_dropdown_search_field.send_keys(c())
    time.sleep(1.5)
    customer_dropdown_search_field.send_keys(Keys.RETURN)

    service_item_dropdown = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".w-row-qbo .activity .select2-container.combo-weekly .select2-chosen")))[1]
    time.sleep(0.5)
    service_item_dropdown.click()
    service_item_dropdown_search_field = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#select2-drop .select2-search .select2-input")))[0]
    service_item_dropdown_search_field.send_keys(c())
    time.sleep(1.5)
    service_item_dropdown_search_field.send_keys(Keys.RETURN)

def get_timesheet_user_profile_three(c):
    customer_dropdown = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".w-row-qbo .select2-container.combo-weekly .select2-chosen")))[4]
    time.sleep(0.5)
    customer_dropdown.click()
    customer_dropdown_search_field = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#select2-drop .select2-search .select2-input")))
    customer_dropdown_search_field.send_keys(c())
    time.sleep(1.5)
    customer_dropdown_search_field.send_keys(Keys.RETURN)

    service_item_dropdown = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".w-row-qbo .activity .select2-container.combo-weekly .select2-chosen")))[2]
    time.sleep(0.5)
    service_item_dropdown.click()
    service_item_dropdown_search_field = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#select2-drop .select2-search .select2-input")))[0]
    service_item_dropdown_search_field.send_keys(c())
    time.sleep(1.5)
    service_item_dropdown_search_field.send_keys(Keys.RETURN)

def y_response(log_box, user_profile, comment, checkbox, c):
    print("Logging Your Normal Weekly Hours Now...")
    user_profile(c)
    checkbox(c)
    logHour = "8"
    log_box()
    for day in log_box():
        day.clear()
        day.send_keys(logHour)
        day.send_keys(Keys.TAB)

    comment(c)

def n_response(log_box, user_profile, comment, checkbox, c):
    user_profile(c)
    checkbox(c)

    print("Please Specify Your Hours Per Weekday")
    specified_monday_hours_input = input("Enter Your Hours For Monday: ").strip()
    specified_tuesday_hours_input = input("Enter Your Hours For Tuesday: ").strip()
    specified_wednesday_hours_input = input("Enter Your Hours For Wednesday: ").strip()
    specified_thursday_hours_input = input("Enter Your Hours For Thursday: ").strip()
    specified_friday_hours_input = input("Enter Your Hours For Friday: ").strip()

    log_box()

    print("Logging Your Specified Hours Now...")
    log_box()[0].clear()
    log_box()[0].send_keys(specified_monday_hours_input)
    log_box()[0].send_keys(Keys.TAB)

    log_box()[1].clear()
    log_box()[1].send_keys(specified_tuesday_hours_input)
    log_box()[1].send_keys(Keys.TAB)

    log_box()[2].clear()
    log_box()[2].send_keys(specified_wednesday_hours_input)
    log_box()[2].send_keys(Keys.TAB)

    log_box()[3].clear()
    log_box()[3].send_keys(specified_thursday_hours_input)
    log_box()[3].send_keys(Keys.TAB)

    log_box()[4].clear()
    log_box()[4].send_keys(specified_friday_hours_input)
    log_box()[4].send_keys(Keys.TAB)

    comment(c)

def c_response():
    print("Copying Last Week's Timesheet Now...")
    copy_last_timesheet = driver.find_element_by_id("btnCopyTimeSheet")
    copy_last_timesheet.click()
    copy_button = driver.find_element_by_css_selector("div.buttons-panel.popup button.ctrl_btn.btn_green")
    copy_button.click()
    #copying takes time to register
    time.sleep(1)

    save_submit_quit()

def lw_response():
    date_dropdown = wait.until(EC.visibility_of_element_located((By.ID, "ddlDateRange")))
    date_dropdown.click()
    date_dropdown.send_keys(Keys.ARROW_UP + Keys.RETURN)

    normal_last_week_response = input("Okay, Did You Work The Normal 8 Hours A Day *LAST* Week For {}? (y/n/c/lw): ".format(client)).strip()
    if normal_last_week_response == "y":
        y_response(get_iterated_log_box, get_timesheet_user_profile, make_a_comment, billable_checkbox, get_client)
    elif normal_last_week_response == "n":
        n_response(get_iterated_log_box, get_timesheet_user_profile, make_a_comment, billable_checkbox, get_client)

    check_for_client_two(get_client_two)
    unbillable_client_three(get_client_three)

    save_submit_quit()

def check_for_client_two(c):
    if c() != "":
        normal_week_response_two = input("Did You Work The Normal 8 Hours A Day This Week For {}? (y/n): ".format(client_two)).strip()
        if normal_week_response_two == "y":
            y_response(get_iterated_log_box_two, get_timesheet_user_profile_two, make_a_comment, billable_checkbox, get_client_two)
        elif normal_week_response_two == "n":
            n_response(get_iterated_log_box_two, get_timesheet_user_profile_two, make_a_comment, billable_checkbox, get_client_two)
    elif c() == "":
        pass

def unbillable_client_three(c):
    if c() != "":
        normal_week_response_three = input("Did You Have Holiday/PTO For {}? (y/n): ".format(client_three)).strip()
        if normal_week_response_three == "y":
            n_response(get_iterated_log_box_three, get_timesheet_user_profile_three, make_a_comment, billable_checkbox, get_client_three)
        elif normal_week_response_three == "n" or "":
            pass

# initiate question for user input to trigger the if statements
print("y = Yes, " + "n = No, " + "c = Copy (Copy Last Week's Timesheet), " + "lw = Last Week (If You Forgot Last Week)")
normal_week_response = input("Did You Work The Normal 8 Hours A Day This Week For {}? (y/n/c/lw): ".format(client)).strip()

# if yes, sends 8 hours each for Monday-Friday; otherwise specify hours
if normal_week_response == "y":
    y_response(get_iterated_log_box, get_timesheet_user_profile, make_a_comment, billable_checkbox, get_client)
elif normal_week_response == "n":
    n_response(get_iterated_log_box, get_timesheet_user_profile, make_a_comment, billable_checkbox, get_client)
elif normal_week_response == "c":
    c_response()
elif normal_week_response == "lw":
    lw_response()

check_for_client_two(get_client_two)
unbillable_client_three(get_client_three)

save_submit_quit()