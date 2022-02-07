#Import modules
import random
import sys
import os


#First part
print ("Hello World")

#Comment
#Multiline comment
'''
Multi
Line
Comments
'''

#Values in the variables can be asign with single or "
#Variables has tu start with letters
#Variables can accept 5 main types: numbers, strings, lists, tuples and dictionaries
name = "José"
name = 'José'
print(name)
name = 15

#7 Algorithmit opperators: +, -, *, /, %(module), **(exponential), //(division and discard remainer)
print("5 + 2 = ", 5+2)
print("5 - 2 = ", 5-2)
print("5 * 2 = ", 5*2)
print("5 / 2 = ", 5/2)
print("5 % 2 = ", 5%2)
print(" 5 ** 2 = ", 5**2)
print("5 // 2 = ", 5//2)

print("1 + 2 - 3 * 2 = ", 1 + 2 - 3 *2)
print("(1 + 2 - 3) * 2 = ", (1 + 2 - 3) * 2)

quote = "\"Always remember you are unique"
multi_line_quote = '''just
like everyone
else\"'''

new_string = quote + multi_line_quote

print(new_string)

print("%s %s %s" %('I like the quote', quote, multi_line_quote))

#Prints a new line
print('\n' * 5)

#With end, that print doesn't add new line at the end
print("I don't like ", end="")
print("newlines.")

#Second part, lists
#Lists are a list of values, and then manipulate them
#Each value has an index (label) (start 0)
#They are shown by []
grocery_list = ["Juice", "Tomatoes", "Potatoes",
"Bananas"]

print("First item:", grocery_list[0])

grocery_list[0] = "Green Juice"
print("First item:", grocery_list[0])

#Printing the subset of the list, from 1 to 3, 3 not included
print(grocery_list[1:3])

other_events = ["Wash Car", "Pick up kids", "Cash Check"]
to_do_list = [other_events, grocery_list]
print(to_do_list)

print((to_do_list[1][1]))

#Is possible to append values
grocery_list.append("Onions")
print(grocery_list)

#Is possible to insert values with an index number
grocery_list.insert(1, "Pickle")
print(grocery_list)

#It can also be removed
grocery_list.remove("Pickle")
print(grocery_list)

#Lists can be sort
grocery_list.sort()
print(grocery_list)

#And reversed
grocery_list.reverse()
print(grocery_list)

#And deleted
del grocery_list[4]
print(grocery_list)

to_do_list2 = other_events + grocery_list

#Length of the list
print(len(to_do_list2))

#The max value of the list. In numbers the highest in strings the letter (W here)
print(max(to_do_list2))

#Same with the min, but the minimun value
print(min(to_do_list2))

#Part 3: Tuples
#Very similar to lists
#Unlike lists, tuples cannot be modified after created
#They are shown by ()
pi_tuple = (3, 1, 4, 1, 5, 9)

tuple_to_list = list(pi_tuple)
list_to_tuple = tuple(tuple_to_list)

print(pi_tuple)
print(tuple_to_list)
print(list_to_tuple)

print(len(list_to_tuple))
print(max(list_to_tuple))
print(min(list_to_tuple))

#Part 4. Dictionaries (or maps)
#Values with an unique key for each value
#Is not possible to join dictionaries, like in list with +
super_villians = {'Fiddler' : 'Isaac Bowin',
'Captain Cold' :'Leonard Snart',
'Weather Wizzard' : 'Mark Mardom',
'Mirror Paster' : 'Sam Scudder',
'Pied Piper' : 'Thomas Peterson'}

#To know the secret identity of the villian
print(super_villians['Captain Cold'])

del super_villians['Fiddler']
print(super_villians)

#Replace information
super_villians['Pied Piper'] = 'Hartley Rathaway'
print(super_villians)
print(len(super_villians))

#Get to get the information of the villain
print(super_villians.get("Pied Piper"))

#Keys print all the first data of the dict
print(super_villians.keys())

#Values is the second data of the dict
print(super_villians.values())

#Part 5. Conditionls
#if else elif with == != > >= <=
age = 30

if age > 16:
    print('You are old enough to drive')
else:
    print('You are not enought old to drive')

if age >= 21:
    print('You are old enough to drive a tractor trailer')
elif age >= 16:
    print('You are old enough to drive a car')
else: print('You are not old enough to drive')

#Logical operators to combine conditions and or not
if ((age >= 1) and (age <= 18)):
    print("You get a birthday")
elif (age == 21 or (age >= 65)):
    print("You get a birthday")
elif not(age == 30):
    print("You don't get a birthday")
else:
    print("You get a birthday party, yeah!")

#Part 6: Looping.
#Perform an action a set number of times
for x in range(0, 10):
    print(x, ' ', end="")

print("\n")

for y in grocery_list:
    print(y)

#It works with both () and []
for x in [2, 4, 6, 8, 10]:
    print(x)

num_list = [[1, 2, 3], [10, 20, 30], [100, 200, 300]]

for x in range(0, 3):
    for y in range(0, 3):
        print(num_list[x][y])

#While loops when I have no idea how many times is gonna loop
#Random number from 0 to 99
random_number = random.randrange(0, 100)

while (random_number != 15):
    print(random_number)
    random_number = random.randrange(0, 100)

print("\n")
i = 0

while (i <= 20):
    if (i%2 == 0):
        print(i)
    elif (i == 9):
        break
    else:
        i += 1
        #Continue will ignore the rest of the code (of the While) and goes to While again
        continue
    i += 1

#Part 7. Functions
#Both reuse and and write more readable code
def addNumbers(fNumber, lNumber):
    sumNumers = fNumber + lNumber
    return sumNumers

print(addNumbers(1, 4))

#Part 8. Some stuff
#Adding a value from the user
print("What is your name?")

#name = sys.stdin.readline()

print("Hello,", name)

#Strings
long_string = "I'll catch you if you fall - The Floor"

#Print the first 4 chars
print(long_string[0:4])
#Print the last 5 chars
print(long_string[-5:])
#Print until the last 5
print(long_string[:-5])

#Concatenate or join 2 strings together using a substring
concatd_string = long_string[:5] + "be there"
print(concatd_string)

#Formating with strings
print("%c is my %s letter and my number %d number is %.5f" %
("X", "favorite", 1, .14))

#Didn't work as I expected
print(long_string.capitalize())

print(long_string.find("Floor"))

#Print if all chars are letters. False for this -
print(long_string.isalpha())

#Print if all chars are numbers
print(long_string.isalnum())

print(len(long_string))

#Replace chars
print(long_string.replace("Floor", "Ground"))
print(long_string)

#Don't know exactly for what is this for
print(long_string.strip())
quote_list = long_string.split(" ")
print(quote_list)

#File IO
#Open first the file
#ab+ to read and append to file
#wb to write file
test_file = open("test.txt", "wb")

#To print the mode used
print(test_file.mode)

#File's name
print(test_file.name)

#To write a file
#How to write in bytes a file
test_file.write(bytes("Write me to this file\n", "UTF-8"))

#Close the file
test_file.close()

#To read a file, it needs to be opened again
#To read and write
test_file = open("test.txt", "r+")

text_in_file = test_file.read()
print(text_in_file)

#It should be closed now?
#Yes
test_file.close()
#Or it cannot be deleted, is being used

#Delete the file
os.remove("test.txt")

#Part 9. Objects
class Animal:
    #attributes
    #Underscore means are private: to change or read them, need funct inside class
    #None is the lack of a value
    __name = None #or ""
    __height = 0
    __weight = 0
    __sound = 0

    #Constructor. Called to set up or init an object
    #self refers itself inside the class
    def __init__(self, name, height, weight, sound):
        self.__name = name
        self.__height = height
        self.__weight = weight
        self.__sound = sound

    #This is called encapsulation
    #Get all the setters, then all the getters
    def set_name(self, name):
        self.__name = name
    
    def set_height(self, height):
        self.__height = height
    
    def set_weight(self, weight):
        self.__weight = weight
    
    def set_sound(self, sound):
        self.__sound = sound
    
    #Getters
    def get_name(self):
        return self.__name

    def get_height(self):
        return str(self.__height)

    def get_weight(self):
        return str(self.__weight)

    def get_sound(self):
        return self.__sound

    #Polymorphism
    def get_type(self):
        print("Animal")

    #Print all te info to the screen
    def toString(self):
        return "{} is {} cm tall and {} kilograms and say {}".format(self.__name,
        self.__height, self.__weight, self.__sound)

cat = Animal("Whiskers", 33, 10, "Meow")

print(cat.toString())

#Inheritance. When ingeritance from another class, gets all the vars, methods and funcs
class Dog(Animal):
    __owner = ""

    def __init__(self, name, height, weight, sound, owner):
        self.__owner = owner
        super(Dog, self).__init__(name, height, weight, sound)

    def set_owner(self, owner):
        self.__owner = owner

    def get_owner(self):
        return self.__owner
    
    def get_type(self):
        print("Dog")

    def toString(self):
        return "{} is {} cm tall and {} kilograms and say {} His owner is {}.".format(self.__name,
        self.__height, self.__weight, self.__sound, self.__owner)

    #Method overloading
    #perform different tasks based on the attributes that are sent in
    def multiple_sounds(self, how_many=None):
        if how_many is None:
            print(self.get_sound())
        else:
            print(self.get_sound() * how_many)

#There is a problem not getting name from parent class
spot = Dog("Spot", 53, 27, "Ruff", "Derek")
#print(spot.toString())

#Polymorphism
#Refer to objects as super class, and then automatically have the correct functions called
class AnimalTesting:
    def get_type(self, animal):
        animal.get_type()

test_animals = AnimalTesting()

#It knows to go to Animal object
test_animals.get_type(cat)

#It knows to go to Dog object
test_animals.get_type(spot)

#Multiple sounds
spot.multiple_sounds(4)
spot.multiple_sounds()