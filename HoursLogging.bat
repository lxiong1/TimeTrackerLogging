@echo off
title Ebillity-Time Tracker
pip install selenium==3.3.3
pip install chromedriver
start C:.\StandAloneServer.bat %*
start C:.\time_tracker_log.py %*