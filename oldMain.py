import sqlite3

connection = sqlite3.connect('myTasks.db')
cursor = connection.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS tasks (id INT, task TEXT, date TEXT, description TEXT)""")

# creates the objects for the classes
class Tasks:

    def __init__(self, task="", date="", description=""):
        self.task = task
        self.date = date
        self.description = description
        self.connection = sqlite3.connect('myTasks.db')
        self.cursor = self.connection.cursor()

    def insertTask(self):

        j=1
        self.cursor.execute("""SELECT * FROM tasks""")
        results = self.cursor.fetchall()
        for task in results:
            j+=1

        self.cursor.execute("""
            INSERT INTO tasks VALUES ('{}','{}','{}','{}')
            """.format(j, self.task, self.date, self.description))
        self.connection.commit()

    def viewTask(self):
        self.cursor.execute("""SELECT * FROM tasks""")
        results = self.cursor.fetchall()
        for task in results:
            print(task)

    def deleteTask(self, taskId):
        selectedTask = taskId
        self.cursor.execute("""DELETE FROM tasks WHERE id = '{}'""".format(selectedTask))
        self.connection.commit()

    def deleteAllTasks(self):
        self.cursor.execute("""DELETE FROM tasks""")
        self.connection.commit()


def start():
    dullTask = Tasks()
    print("=-=-=--=-=-=-=-=-=-=-=-")
    print("Current Tasks:")
    print("     Task, Date, Description")
    dullTask.viewTask()
    print("Options:\n1. Add task\n2. Delete task\n3. Delete All Tasks\n4. Exit")

    selection = input()
    if selection == "1":
        taskName = input("Task name: ")
        taskDate = input("Task date: ")
        taskDescription = input("Task description: ")
        task = Tasks(taskName, taskDate, taskDescription)
        task.insertTask()
        start()
    if selection == "2":
        taskId = int(input("What task have you completed?\n"))
        dullTask.deleteTask(taskId)
        start()
    if selection == "3":
        yesOrNo = input("Do you want to delete all tasks? y/n?\n")
        if yesOrNo == 'y':
            dullTask.deleteAllTasks()
            start()
        if yesOrNo == 'n':
            print("Tasks not deleted")
            start()
    if selection == "4":
        connection.close()
        exit()
    else:
        print("Option not available")
        start()

if __name__ == "__main__":
    start()