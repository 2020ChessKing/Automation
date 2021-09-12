# code
planner = []
due_dates = []
print("\n ------------------------------------\n", "Welcome To The Terminal Planner:", "\n ---------------------------------------------")
def plan():
    print("-------- My Planner --------")
    for i in range(0, len(planner)):
        print(planner[i], "-----", due_dates[i])
    add()

def add():
    assignment = input("Add Something -----> ")
    due_date = input("By When Do You Want to Complete It? -----> ")
    planner.append(assignment)
    due_dates.append(due_date)
    plan()
plan()