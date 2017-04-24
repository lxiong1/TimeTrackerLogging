The script is written in python for the purposes of automating hours on eBillity.
Please look at the requirements below for running the script.

REQUIREMENTS
------------
*PLACE downloaded/cloned time_tracker_log folder on desktop
*INSTALL Python Interpreter (Already in C:Users\<ProfileName>\Desktop\time_tracker_log\Python Install)
	*NECESSARY to add python interpreter to PATH when installing; this makes the python interpreter a system environment variable to compile python code
	*Make sure to download 32-bit or 64-bit corresponding to your computer's specifications
	*By default, Pip (package installer for Python) comes with python interpreter
*MOVE provided chromedriver.exe to C:\Python36\Scripts
*ADD/CHANGE email in JSON file according to your eBillity login credentials
*ADD your user profile in JSON file provided if it doesn't exist and format it accordingly
	*This will include your name, email, and client(s)

RUNNING THE SCRIPT
------------------
*There are .bat (for Windows OS) and .sh(for Unix-based OS) file for running the python script 
*The script will provide instructions and will need user input according to user's hour logging needs
*The password prompt during script will be ***INVISIBLE***