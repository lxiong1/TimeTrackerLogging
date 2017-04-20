The script is written in python for the purposes of automating hours on eBillity.
Please look at the requirements below for running the script.

REQUIREMENTS
------------
*Install Python Interpreter (*Already in dependencies folder*)
	*NECESSARY to add python interpreter to PATH when installing; this makes the python interpreter a system environment variable to compile python code
	*By default, Pip (package installer for Python) comes with python interpreter
*Download and Install Selenium WebDriver for Python
	*Use the command in the command line to install Selenium WebDriver
		pip install selenium
*Download and Install ChromeDriver
	*Use the command in the command line to install ChromeDriver
		pip install chromedriver_installer
*ADD/CHANGE email in JSON file according to your eBillity login credentials
*ADD your user profile in JSON file provided if it doesn't exist and format it accordingly
	*This will include your name, email, and client(s)

RUNNING THE SCRIPT
------------------
*The Selenium Standalone Server NEEDS to be running first before running the script
	*Either double-click the server .jar or run the server through the command line
*The TimeTrackerLogging.py script can be run directly by opening with the python interpreter 
*There are also a .bat (for Windows OS) and .sh(for Unix-based OS) file for running the python script 
*The script will provide instructions and will need user input according to user's hour logging needs