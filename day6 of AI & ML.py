# for loop#
#for variable in  range(start  ,stop ,step):
# code repart
for i in range(5,0,-1):
    print(i)
  
for i in range(5,0,1):
    print(i)
    
#while syntax#
#while(condition)

count = 0
while count > 5:
    print(count)
    count -= 1

print(" increasement order  ")
while count < 5 :
    print (count )
    count +=1
    
import time 

for i in range(10,0,-2):
    print(i)
    time.sleep(2)
print("happy new year")


# project 5

import time 

start =int(input("enter the time:"))

print("\n countdown")

while start >0 :
    print(start)
    time.sleep(1)
    start-=1
    
    
print ("\n----happy new year!---10")