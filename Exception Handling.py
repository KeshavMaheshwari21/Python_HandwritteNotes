name = input('Please enter your name : ')
print(name)
age=int(input('Please enter your age : ')) # Twenty
print("My name is",name,"and I am",age,'years old')
print('Imp line 1')
print('Imp line 2')
print('Imp line 3')
print('Imp line 4')

# It is a unwanted situation that disturb the program execution
# Exception Handling
# try , except , else , finally

try:
    name = input('Please enter your name : ')
    print(name)
    age=int(input('Please enter your age : ')) # Doubtfull
    print("My name is",name,"and I am",age,'years old')

except: 
    print('Error is occured')

else: 
    print('Error is not occured')

finally: # Always
    print('Finally printed')

print('Imp line 1')
print('Imp line 2')
print('Imp line 3')
print('Imp line 4')
print('Imp line 5')
print('Imp line 6')