The script is written in python for the purposes of automating hours on eBillity through a headless browser using PhantomnJS Driver.
Please look at the requirements below for running the script.

REQUIREMENTS
------------
*Selenium Standalone Server (*Already provided in folder*)
*Download and Install latest Python Interpreter (https://www.python.org/downloads/release/python-360/)
	*NECESSARY to add python interpreter to PATH when installing; this makes the python interpreter a system environment variable to compile python code
*Download and Install Selenium WebDriver for Python (https://pypi.python.org/pypi/selenium)
*Download and Install PhantomJS Driver (http://phantomjs.org/download.html)
	*Change the phantomjs.binary.path in the python script under <desired_caps_value> to the file path on your local computer
*CHANGE email and password in python script to your own personal login credentials (email is stored in eBillityUserProfiles.json)
	*Note: I am using the keyring library to encrypt my password; it is not necessary but recommended to do so
	*For information on how to setup keyring ((https://pypi.python.org/pypi/keyring))
	*If NOT using keyring, please remove anything keyring related in the script and replace it with your own password value
		Example: email = employee_data["Lue Xiong"]["email"]
				 password = "donutsarelife"
				 login_email_field.send_keys(email + Keys.TAB + password + Keys.ENTER)
*CHANGE method get_client() to your name
	Example: client = employee_data["Your Name"]["client"]

RUNNING THE SCRIPT
------------------
*The Selenium Standalone Server NEEDS to be running first before running the script
	*Either double-click the server .jar or run the server through the command line
*The TimeTrackerLogging.py script can be run directly by opening with the python interpreter 
*There are also a .bat (for Windows OS) and .sh(for Unix-based OS) file for running the python script 
*The script will provide instructions and will need user input according to user's hour logging needs

NOTE TO SELF:
Unbillable Hours ***Needs to account for 2nd and 3rd box***
Comments Section ***Needs to account for 2nd and 3rd comment box***
Logging last weeks Hours ***Done***
Project Selection - User Profiles JSON file***Needs to account for multiple clients***
Calender communication with code ***Maybe not viable?***