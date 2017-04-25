@echo off
title Ebillity-Time Tracker
pip install selenium==3.3.3
start C:.\HideBat.vbs %*
start C:.\time_tracker_log.py %*