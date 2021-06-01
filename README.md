# extract_from_filename
import os  print("Remember to cd to wherever your files are, before running this program!!") files = os.listdir("/Users/vedansh/Desktop/files")  landmark = input("Landmark for files (will get files before this character):     ")  for file in files:     pos_of_landmark = file.find(landmark)     account_number = file[:pos_of_landmark]     print(account_number)
