import json
import datetime

def tasks():
    f = open("tasks.txt", "r")
    allTaskFile = f.read()
    f.close()

    primitiveTaskList = allTaskFile.split("\n")

    taskList = []
    for x in primitiveTaskList:
        taskList.append(json.loads(x))

    for i in range(0, len(taskList)):
        print("==================")
        print("Task name: " + taskList[i]["name"])
        print("Description: " + taskList[i]["desc"])
        print("Creation date: " + taskList[i]["creation"])
        print("Goal date: " + taskList[i]["goal"])
        print("==================")

def create():
    print("CREATE A TASK: ")
    taskName = input("Task Name: ")
    desc = input("Description: ")
    creationNonFormat = datetime.datetime.today()
    goal = input("Goal date (DD/MM/AAAA): ")

    newCreation = str(creationNonFormat.day) + "/" + str(creationNonFormat.month) + "/" + str(creationNonFormat.year)

    x = {
        "name": taskName,
        "desc": desc,
        "creation": newCreation,
        "goal": goal
    }

    f = open("tasks.txt", "a")
    f.write("\n" + str(json.dumps(x)))
    f.close()


def remove(taskName):
    formatName = taskName.lower()
    f = open("tasks.txt", "r")
    allTaskFile = f.read()
    f.close()

    primitiveTaskList = allTaskFile.split("\n")

    taskList = []
    for x in primitiveTaskList:
        taskList.append(json.loads(x))

    for i in range(len(taskList)):
        if taskList[i]["name"].lower() == formatName:
            del taskList[i]
            break

    f = open("tasks.txt", "w")
    f.write("")
    f.close()

    f = open("tasks.txt", "a")
    for index, x in enumerate(taskList):
        if index < len(taskList) - 1:
            y = json.dumps(x)
            f.write(y + "\n")
        else:
            y = json.dumps(x)
            f.write(y)
    f.close()
    
    
def complete(taskName):
    formatName = taskName.lower()
    f = open("tasks.txt", "r")
    allTaskFile = f.read()
    f.close()

    primitiveTaskList = allTaskFile.split("\n")

    taskList = []
    for x in primitiveTaskList:
        taskList.append(json.loads(x))

    f = open("completed.txt", "a")
    for i, x in enumerate(taskList):
        if taskList[i]["name"].lower() == formatName:
            y = json.dumps(x)
            f.write("\n" + y)
            del taskList[i]
            break
    f.close()

    f = open("tasks.txt", "w")
    f.write("")
    f.close()

    f = open("tasks.txt", "a")
    for index, x in enumerate(taskList):
        if index < len(taskList) - 1:
            y = json.dumps(x)
            f.write(y + "\n")
        else:
            y = json.dumps(x)
            f.write(y)
    f.close()

def completed():
    f = open("completed.txt", "r")
    allTaskFile = f.read()
    f.close()

    primitiveTaskList = allTaskFile.split("\n")

    taskList = []
    for x in primitiveTaskList:
        taskList.append(json.loads(x))

    for i in range(0, len(taskList)):
        print("==================")
        print("Task name: " + taskList[i]["name"])
        print("Description: " + taskList[i]["desc"])
        print("Creation date: " + taskList[i]["creation"])
        print("Goal date: " + taskList[i]["goal"])
        print("==================")

if __name__ == "__main__":
    print("WELCOME AGAIN")
    action = ""

    while action != "exit":
        action = input("What do you wanna do?: ")
        if action == "list":
            tasks()
        elif action == "create":
            create()
        elif action == "remove":
            taskName = input("Enter the task name: ")
            remove(taskName)
        elif action == "complete":
            taskName = input("Enter the task name: ")
            complete(taskName)
        elif action == "completed":
            completed()
        elif action == "help":
            print("You can ask for 'list', 'create', 'remove, 'complete', 'completed' or 'exit'")
        elif action == "exit":
            print("Vuelve pronto")
            break
        else: 
            print("Please enter a valid instruction")
        action = ""