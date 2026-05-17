import os
import json
import sys

if not os.path.exists("tasks.json"):
    with open("tasks.json", "w") as file:
        json.dump([], file)

command = sys.argv[1]

if command == "add":
    print("Adding task...")
elif command == "list":
    print("Listing tasks...")
else:
    print("Unknown command")

