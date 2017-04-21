@echo off
title Ebillity-Time Tracker
pip install selenium==3.3.3
pip install chromedriver
start C:.\InvisibleBAT.vbs %*
python C:.\time_tracker_log.py %*