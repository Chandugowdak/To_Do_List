lis = []  # INITIALIZE AN EMPTY LIST 'lis'

print("Enter the Task You Have To Do")  # PROMPT USER TO ENTER TASKS TO DO
for i in range(0, 6):  # LOOP 6 TIMES TO GET 6 TASKS
    Work_To_Done = input()  # GET USER INPUT FOR EACH TASK
    lis.append(Work_To_Done)  # ADD EACH TASK TO THE LIST 'lis'

for i in range(0, len(lis)):  # LOOP THROUGH THE LENGTH OF THE LIST 'lis'
    print("Enter 10 if the work is not done: ")  # PROMPT USER TO ENTER 10 IF WORK IS NOT DONE
    Work_Completed = int(input("Enter the Work Has Completed: "))  # GET USER INPUT FOR COMPLETED WORK AS AN INTEGER
    if Work_Completed == 10:  # IF USER INPUT IS 10
        break  # BREAK OUT OF THE LOOP
    del lis[Work_Completed]  # DELETE THE TASK AT THE INDEX SPECIFIED BY USER INPUT

for i in range(0, len(lis)):  # LOOP THROUGH THE LENGTH OF THE LIST 'lis'
    print(lis[i])  # PRINT EACH REMAINING TASK IN THE LIST
