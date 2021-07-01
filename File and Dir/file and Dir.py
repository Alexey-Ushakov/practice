import os, sys
print("CWD: ", os.getcwd())
print("Script: ", sys.argv[0])
print(".EXE: ", os.path.dirname(sys.executable))
print("Script dir: ", os.path.realpath(os.path.dirname(sys.argv[0])))
pathname, scriptname = os.path.split(sys.argv[0])
print("Relative script dir: ", pathname)
print("Script dir: ", os.path.abspath(pathname))
print('Current file: ', os.path.dirname(__file__))
print(os.path.dirname(__file__) + '/IDLESTARTUP.txt')

print(os.path.dirname(__file__))  # Путь к файлу
print(os.path.normpath(__file__))  # Путь к файлу
print(os.path.abspath(__file__))  # Путь к файлу