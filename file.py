import keyboard, time, pyperclip
import sys
import os

class bcolors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    END = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

path = "/Users/Gavin/Desktop"
dirlist = os.listdir(path)

print(f"{bcolors.HEADER}Type 'ls' to view everything in the dir{bcolors.END}")
print(f"{bcolors.HEADER}Or type the file you want to find! File is case sensitive! \nIf you're not sure how its spelt, type the first few letters and it will display all files that start with the first letters!\n{bcolors.END}")

program = "running"

while program == "running":

    question = input("File >> ")

    if question == "ls":
        print(dirlist) 
    
    if question == question:
        breakdown = list(question)
        print(f"\n{bcolors.GREEN}Finding files that start with {breakdown[0]}! {bcolors.END}\n")
        for file in dirlist:
            if file.startswith(breakdown[0]):
                print(f"{bcolors.WARNING}{file}{bcolors.END}")
        time.sleep(2)
        print(f"\n{bcolors.GREEN}Finding files that start with: {breakdown[0]} and {breakdown[1]}! {bcolors.END}\n")
        for file2 in dirlist:
            if file2.startswith(breakdown[0] + breakdown[1]):
                print(f"{bcolors.WARNING}{file2}{bcolors.END}")
        # if question != dirlist:
        #     print("Could not find file, did you type it correctly?")


    if question == "test":
        print(breakdown[0])
    
    # if question == question:
    #     if question in dirlist:
    #         print("Yep!")
    #     else:
    #         print("Nope!")

if program == "stop":
    print("Stopping program!")
