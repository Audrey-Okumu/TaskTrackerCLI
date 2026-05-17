import os
import json
import sys

#Automatically create .json file
if not os.path.exists("tasks.json"):
    with open("tasks.json", "w") as file:
        json.dump([], file)

#load existing tracks
with open("tasks.json", "r") as file:
    tasks = json.load(file)

command = sys.argv[1]

if command == "add":
    print("Adding task...")
elif command == "list":
    print("Listing tasks...")
else:
    print("Unknown command")

command = sys.argv[2]