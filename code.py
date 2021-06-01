import os

file_location = input("Input your path for folder with files:    ")
files = os.listdir(file_location)

landmark = input("Landmark for files (will get files before this character):     ")

for file in files:
    pos_of_landmark = file.find(landmark)
    values_before_landmark = file[:pos_of_landmark]
    print(values_before_landmark)
