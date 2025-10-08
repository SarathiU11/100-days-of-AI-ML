<<<<<<< HEAD
shopping_list = ["milk","eggs","bread"]
print(shopping_list)


#shopping list print using a indesx of the number 
shopping_list = ["milk","eggs","bread"]
print(shopping_list[0])
print(shopping_list[1])
print(shopping_list[2])

#append
shopping_list.append("butter")
print(shopping_list)

#insert
shopping_list.insert(1,"juice")
print(shopping_list ) 

#remove
shopping_list.remove("bread")
print(shopping_list)

#pop
#shopping_list.pop()
#print(shopping_list)

#looping through the list 

for item in enumerate (shopping_list):
    print(item)
   
   
   
# project shooping list 

shop_list=[]

def show_menu():
    print("\n----shopping list menu---")
    print("1.view the shopping list")
    print("2. add the item")
    print("3.remove the item")
    print("4. clear list ")
    print("5.exit")
    
 while true:
     show_menu()
     choice = input(int("enter the choice (1-5):"))
      
      if choice =="1":
         print("\n---shopping list --)
         if not shop_list:
           print("you shopping list is empty")
          else:
            for index item enumerate (shopping_list):
             print(F"{index + 1} .{items}")
=======
shopping_list = ["milk","eggs","bread"]
print(shopping_list)


#shopping list print using a indesx of the number 
shopping_list = ["milk","eggs","bread"]
print(shopping_list[0])
print(shopping_list[1])
print(shopping_list[2])

#append
shopping_list.append("butter")
print(shopping_list)

#insert
shopping_list.insert(1,"juice")
print(shopping_list ) 

#remove
shopping_list.remove("bread")
print(shopping_list)

#pop
#shopping_list.pop()
#print(shopping_list)

#looping through the list 

for item in enumerate (shopping_list):
    print(item)
   
   
   
# project shooping list 

shop_list=[]

def show_menu():
    print("\n----shopping list menu---")
    print("1.view the shopping list")
    print("2. add the item")
    print("3.remove the item")
    print("4. clear list ")
    print("5.exit")
    
 while true:
     show_menu()
     choice = input(int("enter the choice (1-5):"))
      
      if choice =="1":
         print("\n---shopping list --)
         if not shop_list:
           print("you shopping list is empty")
          else:
            for index item enumerate (shopping_list):
             print(F"{index + 1} .{items}")
>>>>>>> 7127049db63ac27d43c1052f46db5254d0bbc422
  