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
        print("=========")
        print("Task name: " + taskList[i]["name"])
        print("Description: " + taskList[i]["desc"])
        print("Creation date: " + taskList[i]["creation"])
        print("Goal date: " + taskList[i]["goal"])
        print("=========")

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
    print("remove")

def complete(taskName):
    print("complete")

if __name__ == "__main__":
    print("WELCOME AGAIN")
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
    else: 
        print("enter a valid instruction")