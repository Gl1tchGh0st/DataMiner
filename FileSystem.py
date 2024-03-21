import os

def fileSystem():
    directory = os.path.expanduser('~') # Change for purpose
    os.chdir(directory)
    os.system("tree")