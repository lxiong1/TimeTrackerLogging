@echo off
title Ebillity-Time Tracker
pip install selenium==3.3.3
pip install chromedriver
python C:.\time_tracker_log.py %*
pause