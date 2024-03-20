import os

def shutdown():
    if os.name == 'posix':  # Linux or macOS
        os.system('sudo shutdown now')
    elif os.name == 'nt':   # Windows
        os.system('shutdown /s')
    else:
        raise OSError("Unsupported operating system")