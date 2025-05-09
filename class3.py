'''
1. Data types
Outline:
Write a program to find what type of datatype the given variable is?
'''
a = "Hello"
print("The data type of A is: ", type(a))
b = 10
print("The data type of B is: ", type(b))
c = 3.1415
print("The data type of C is: ", type(c))
d = True
print("The data type of D is: ", type(d))

'''
2. Typecasting
Outline:
Write a program to change the datatype of given variables?
'''
string = "Dakshith"
integer = 99
float = 1.414
boolean = False
print(type(string))
print(type(integer))
print(type(float))
print(type(boolean))
#print(int(string))
#Strings cannot be converted into an integer but and integer can be converted into a string
integer1 = str(integer)
print(type(integer1))
float1 = int(float)
print(type(float1), float1)
#string1 = int(string)
#print(type(string1))
bool1 = int(boolean)
print(type(bool1), print(bool1))

'''
3. String operation
Outline:
Write a program to print the “CODINGAL” word in a reverse direction.
'''
codingal = "CODINGAL"
print(codingal[::-1])


word = "under"
print(word[2])
print(word[4])
print(word.index("e"))
#slicing:
variable = "Hello World"
print(variable[1:4])
print(variable[:5])
print(variable[6:])
a = "characteristics"
print(a.index("i"))
print(a[::5])
print(a[::-1])
print(a[0::2])
b = "Dakshith"
c = "Karthikeyan"
print(b+" "+c)