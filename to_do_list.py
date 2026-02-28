while True:
 
 user_choice=input("do you want to add a new To-Do item?(y/n):")
 if user_choice == "exit":
    print("thank you for using the To-Do program, come back again soon")
    break
 
 if user_choice.lower() == "y":
  new_content=input("type in your new To-Do item : ")
  with open("to_do.txt","a",encoding="utf-8") as file:
   file.write(new_content + "\n")

 elif user_choice.lower() == "n":
   show_list = input("do you want to list your To-Do items? (y/n) : ").lower()
   if show_list == "y":
     with open("to_do.txt", "r",encoding="utf-8") as file:
        show_content = file.read()
        print("\nyour To-Do items :")
        print(show_content)



