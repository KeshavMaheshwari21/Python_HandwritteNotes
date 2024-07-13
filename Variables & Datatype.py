# Variables is a small block of memory container 
# In C language int var = 10;
# In python no need of defining datatype

var = 10
print(var)

# #To check datatype of the variable

print(type(var))

# Rules for declaring the variable
# 1. A-Z , a-z , 0-9 , _ only these characters can be used
# 2. Variable name cannot start with number
# 3. Variable name is case sensitive AGE = 10 , Age = 23 , age = 90 (all are different)
# 4. A variable name cannot be any of the Python keywords

# There are Some Reserved Keywords in Python whch cannot be used as a Variable

var1 = 20
var2 = 30

# Datatypes 

# For declaring a String variable the quotes is used weather double single 
st = "Upflairs" # string
print(type(st))
print(st)

# [] brackets is used for indexing in Python
# Space( ) is also given index in Pyhton

st = "Upflairs"
print(st[4])

# WE WANT TO PRINT (air) FROM (Upflairs)
# For printing the Substring we need to find the starting point and the ending point
# start = 4 , end = 6+1(it doesn't consider the ending index)
print(st[4:7:2]) # [starting : stoping : jump] jump is by default 1

# Indexing is two types
# 1. Positive Indexing (Forward) [0 - end]
# 2. Negative Indexing (Backward) [-1 - start]

print(st[4]) # (+ve Indexing)
print(st[-4]) # (-ve Indexing)

# print(st[2:]) --> In this case if the stoping point is not defined then it will go till end
# print(st[:4]) --> In this case if the startingpoint is not defined then it will start from 0

# print(st[::-1]) --> In this case the st will be print in reverse order

st = "Upflairs pvt ltd jaipur Rajasthan"

print(st[-16:-10])

# len function is used to get the length of the String
print(len(st))

# count function is used to find the number of occurrence of any Character/String in the variable
print(st.count("Rajasthan"))

# Lower function is used to conver all the character in lower character
# Upper function is used to convert all the character in upper character
print(st)
print(st.upper())
print(st.lower())


# ASSIGNMENT 1

# The title() method returns a string where the first character in every word is upper case. Like a header, or a title.If the word contains a number or a symbol, the first letter after that will be converted to upper case.
print(st.title())

# The first character is converted to upper case, and the rest are converted to lower case UPFLAIRS --> Upflairs
print(st.capitalize())


# Replace function is used to replace the string from the given string
print(st.replace('Upflairs','Flipkart'))

# We can also remove by not passing the removing string
print(st.replace('Upflairs',''))

# Find function is used to find the index of the any character/string
print(st.find('u'))

# ASSIGNMENT 2

# The startswith() method returns True if the string starts with the specified value, otherwise False --> string.startswith(value, start, end)
print(st.startswith("U"))

# The split() method splits a string into a list --> string.split(separator, maxsplit)
st.split()

# The strip() method removes any leading, and trailing whitespaces --> string.strip(characters)
st.strip()

# The center() method will center align the string, using a specified character (space is default) as the fill character --> string.center(length, character)
st.center()

# The endswith() method returns True if the string ends with the specified value, otherwise False --> string.endswith(value, start, end)
st.endswith()

#  BOOLEAN DATATYPE 

# When in any variable True/False is stored then it is defined as boolean datatype
# In boolean only True/False is stored
# var1 = True
# var2 = False
print(var1,var2)
print(type(var1),type(var2))

#  LIST DATATYPE
# LIST is an alternative of ARRAY
# LIST is collection of variable but not similar datatype
# LIST is of dynamic & referential nature ( Size is not fixed & can store multiple datatype )

# Declaring a list
ls = [12,23,45,54,1.2,1.3,1.21,'upflairs',True] 
print(ls)
print(type(ls))

# Indexing is same as string
ls = [10,12,13,14,'Upflairs',16]
print(ls[4][4:7])

# Mutable - changable (LIST)
# Immutable - unchangable

# Changing the first index in the list

student_name=['taniya','yash','prerna','ruchika','aditya','kalika','yash']

student_name[0] = 'Tanya' # manipulation / updation

# Append function is used to add the data in list in python & inserts data at last position
student_name.append('ritu')

# Pop function is used to remove the item from the last position
student_name.pop()

# Insert function is used to insert element at given index and rest of the items are shifted
student_name.insert(1,'gurpreet')

# Remove function is used to remove the item from the list
student_name.remove('prerna')

# Del function is used to remove the item by giving the index in the list
del student_name[2]

# Count function is used to print number of time the item is present
print(student_name.count('yash'))

ls1 = ['A','B','C','D','E']
ls2 = [1,2,3,4,5,6,8,7]

# Reverse function is used to reverse the list
ls1.reverse()
print(ls1)

# Sort function is used to sort the list
ls2.sort() # Ascending Order
ls2.sort(reverse=True) # Descending order
print(ls2)

# Min is an aggregate function used to find minimum in list
print(min(ls2))

# Max is an aggregate function used to find maximum in list
print(max(ls2))

# Sum function is used to find sum of all items in the list
print(sum(ls2))

ls2 = ['F','G']
print(ls1+ls2)

ls1.append(ls2)
ls1.extend(ls2)
print(ls1)

ls1 = ['A','B','C','D','E']

ls1.clear()

print(ls1.index('C'))

ls2=[10,20,3.1,'upflairs pvt ltd',500,400]

ls2[2]=100
print(ls2[3][0:8])
ls2[ls2.index('upflairs pvt ltd')]="flipkart pvt ltd"
print(ls2)


#           TUPLE
# TUPLE ARE IMMUTABLE unchangeable


tp1 = (25,12,14,45,"upflairs",True,2.2)
tp1.count()
tp1.index()
print(type(tp1))


# <<<<<<<<<<<<   SET   >>>>>>>>>>>>
# SET does not allow duplicate items


st = {32,2,1,4,5,6,54,65,76,54,7,54}
print(type(st))

st.add(5000)

st.remove(54)

st.discard(54)

st1 = {52,41,63,96,78,54}
st2 = {52,41,65,55,22}

st1.update(st2) # st1 + st2

st1.intersection(st2)

print(st1.intersection(st2))


# <<<<<<<<   DICITIONARY   >>>>>>>
# pairs = (key:value)

marks = {'mohit':90,'rohit':69,'rokcy':89,'keshav':99}
print(type(marks))

# Duplicate key is not allowed but duplicate value is allowed

marks = {'mohit':90,'rohit':69,'rokcy':89,'keshav':99}
print(type(marks))
print(marks)

# The key is passed in [] brackets to get the value
print(marks['mohit'])

# Updation of the value in dictionary
marks['mohit'] = 65
print(marks['mohit'])

# If the key is not present then it will be inserted in the dictionary
marks['rahul']=40 # Insertion
print(marks)

marks = {'mohit':90,'rohit':69,'rokcy':89,'keshav':99}

# .keys() method is used to access only keys in dictionary
print(marks.keys())

# .values() method is used to access only values in dictionary
print(marks.values())

# pop() method is used to remove the pair by passing the key of that pair
marks.pop('mohit')
print(marks)

# Removing the name ritu and marks 336 from the Dictionary
students = {'Name':['rahul','mohit','ritu','yash','jugnu'],
            'Marks':[52,14,36,45,96],
            'Subject':"Science"}
students['Marks'][1]=41
print(students)


# ____________TYPECASTING__________


# The changing of the varaible's datatype fron int -> float is called TYPECASTING

# Int(), float(), str(), tuple(), list(), dict(), set()
num1 = 10 # Int
num1=float(num1) # Changing to the Float data type
print(num1)
print(type(num1))
