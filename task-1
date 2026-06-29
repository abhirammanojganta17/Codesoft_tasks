tasks =[]
while True :
  print("\n1.Add Task")
  print("2.view Task")
  print("3.Remove Task")
  print("4.Exit")
  choice = int(input("Enter Your Choice:"))

  if choice == 1:
    task = input("Enter Task:")
    tasks.append(task)
    print("Task Added")
    
  elif choice == 2:
     print("Tasks:",tasks)
     
  elif choice == 3:
     task = input("Enter task to Remove:")
     if task in tasks:
         tasks.remove(task)
         print("Task removed")
     else:
        print("Task not found")
    
  elif choice == 4:
     print("Exit")
     break
  else:
     print("invalid choice")
