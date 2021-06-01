import os

file_location = input("Input your path for folder with files:    ")
files = os.listdir()

landmark = input("Landmark for files (will get files before this character):     ")

for file in files:
    pos_of_landmark = file.find(landmark)
    account_number = file[:pos_of_landmark]
    print(account_number)
