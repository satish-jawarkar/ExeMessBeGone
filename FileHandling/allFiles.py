import os

current_file = os.getcwd()
print(current_file)

allFiles = os.listdir(current_file)
print(allFiles)

for file in allFiles:
    print(file)
    if os.path.isdir(file):
        print("ayyyyyyyooooooooooo")

