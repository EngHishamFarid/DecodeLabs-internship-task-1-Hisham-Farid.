tasks=[]
while True:
    a=int(input("Press 1 to view your tasks list \nPress 2 to add a task   \nPress 3 to delete an accomplished task  \npress 4 to exit \n"))
    if a == 1 and len(tasks)==0:
          print("your tasks list is empty")
    if a == 1 and len(tasks)!=0:
        for i in range (len(tasks)) :
            print(f"{i+1} : {tasks[i]}")
    elif a == 2 : 
            tasks.append(input("Enter your new task\n"))
            print ("THE NEW TASKS LIST IS ") 
            for k in range (len(tasks)) :
                print (f"{k+1} : {tasks[k]}")
    elif a == 3 and len(tasks)==0:
         print("your tasks list is already empty , try again")
         
    elif a == 3  :
        print ("congrats for accomplishing a new task , your tasks list is \n ")
        for l in range (len(tasks)) :
            print(f"{l+1} :{tasks[l]}\n" )
        b=int (input(" Enter your accomplished task number\n")) -1  
        tasks.remove(tasks[b])
        print ("THE NEW TASKS LIST IS ") 
        for k in range (len(tasks)) :
            print (f"{k+1}: {tasks[k]}") 
    elif a == 4 :
         break 
    else: 
         print("wrong number , try again")