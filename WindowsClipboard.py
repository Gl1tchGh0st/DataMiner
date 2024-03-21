import win32clipboard

def getClipBoard():
    win32clipboard.OpenClipboard()
    data = win32clipboard.GetClipboardData()
    win32clipboard.CloseClipboard()
    print(data) # Could also be written to file for saving periodically


def writeClipBoard():
    data = "Data to write to clipboard here"
    win32clipboard.OpenClipboard()
    win32clipboard.EmptyClipboard()
    win32clipboard.SetClipboardText('testing 123')
    win32clipboard.CloseClipboard()