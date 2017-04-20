#!/usr/bin/env python
pip install -U selenium==3.3.3
pip install -U chromedriver
chmod +x StandAloneServer.bat
chmod +x time_tracker_log.py
start StandAloneServer.bat
python time_tracker_log.py