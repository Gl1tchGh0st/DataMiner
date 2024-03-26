import os
import win32com.client

script_path = "./Script.py"
shell = win32com.client.Dispatch("WScript.Shell")
shortcut = shell.CreateShortcut(os.path.join(os.environ["APPDATA"], "Microsoft", "Windows", "Start Menu", "Programs", "Startup", "Script.lnk"))

# Set the shortcut properties
shortcut.Targetpath = "pythonw.exe"  # Use "pythonw.exe" to run the script without a console window
shortcut.Arguments = script_path
shortcut.IconLocation = script_path  # Optional: Set the icon for the shortcut
shortcut.WindowStyle = 7  # 7 = minimized
shortcut.save()
