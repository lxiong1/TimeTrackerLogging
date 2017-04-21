Dim WinScriptHost
Set WinScriptHost = CreateObject("WScript.Shell")
WinScriptHost.Run Chr(34) & "C:\Users\luexi\Desktop\time_tracker_log\StandAloneServer.bat" & Chr(34), 0
Set WinScriptHost = Nothing