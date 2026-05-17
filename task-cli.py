import os
import json
import sys
from datetime import datetime

#Automatically create .json file
if not os.path.exists("tasks.json"):
    with open("tasks.json", "w") as file:
        json.dump([], file)

#load existing tracks
with open("tasks.json", "r") as file:
    tasks = json.load(file)

# Check if command exists
if len(sys.argv) < 2:
    print("Usage: python task_tracker.py <command>")
    sys.exit()

command = sys.argv[1]

if command == "add":
    if len(sys.argv) < 3:
        print("Please provide a task description.")
        sys.exit()

    description = sys.argv[2]

    new_task = {
        "id": len(tasks) + 1,
        "description": description,
        "status": "todo",
        "createdAt": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "updatedAt": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    tasks.append(new_task)

    # Save back to JSON
    with open("tasks.json", "w") as file:
        json.dump(tasks, file, indent=4)

    print(f"Task added successfully (ID: {new_task['id']})")
elif command == "list":
    print("Listing tasks...")
else:
    print("Unknown command")
