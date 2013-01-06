# Exercises for chapter 3: Problems 3.1, 3.2, 3.3, and 3.4 in Think Python

# Name: Sidd Tewari

# Exercise 3.1. Move the last line of this program to the top, 
# so the function call appears before the definitions. 
# Run the program and see what error message you get.

#SOLUTION

# moving repeat_lyrics() - the function call above the function definition leads to an error message

# error message:
# Traceback (most recent call last):
#   File "chapThree.py", line 5, in <module>
#     repeat_lyrics()
# NameError: name 'repeat_lyrics' is not defined

# repeat_lyrics() - commented out, so that the rest of the program can be executed

def print_lyrics():
    print "I'm a lumberjack, and I'm okay."
    print "I sleep all night and I work all day."

def repeat_lyrics():
    print_lyrics()
    print_lyrics()

print
print 'EXERCISE 3.1:'
print 'TESTED and COMMENTED OUT BECAUSE of the ERROR MESSAGE'
print "ERROR MESSAGE received - 'repeat_lyrics' is not defined WHEN FUNCTION CALL MOVED ABOVE FUNCTION DEFINTION"
print
#-------------------------------------------------------------------------------

# Exercise 3.2. Move the function call back to the bottom and 
# move the definition of print_lyrics after the definition of 
# repeat_lyrics. What happens when you run this program?

def repeat_lyrics():
    print_lyrics()
    print_lyrics()

def print_lyrics():
	print "I'm a lumberjack, and I'm okay."
	print "I sleep all night and I work all day."

print 'EXERCISE 3.2, LYRICS:'
repeat_lyrics()
print

#--------------------------------------------------------------------------------

# Exercise 3.3. Python provides a built-in function called len that returns the length of a string, so
# the value of len('allen') is 5.
# Write a function named right_justify that takes a string named s as a parameter and prints the
# string with enough leading spaces so that the last letter of the string is in column 70 of the display.
# >>> right_justify('allen')

def right_justify(s):
	a = len(s)
	b = 70-a
	print " "*b, s
	
print 'EXERCISE 3.3, RIGHT ALIGNMENT:'	
right_justify('allen')
right_justify('benjamin walker')
right_justify('rehman romano aligator wash')
right_justify('hi')
print

#---------------------------------------------------------------------------------------

# Exercise 3.4. A function object is a value you can assign to a variable or pass as an argument. 
# For example, do_twice is a function that takes a function object as an argument and calls it twice:
# def do_twice(f):
#     f()
#     f()
# Here's an example that uses do_twice to call a function named print_spam twice.
# def print_spam():
#     print 'spam'

# do_twice(print_spam)

#1. Type this example into a script and test it. - TESTED

def do_twice(f):
	f()
	f()
	
def print_spam():
	print 'spam'

print 'EXERCISE 3.4, PROBLEM 1 - TESTED:'	
do_twice(print_spam)
print

# 2. Modify do_twice so that it takes two arguments, a function object and a value, and calls the function twice, 
# passing the value as an argument.
# 3. Write a more general version of print_spam, called print_twice, that takes a string as a parameter and prints it twice.
# 4. Use the modified version of do_twice to call print_twice twice, passing 'spam' as an argument

def do_twice(f,v):
	f(v)
	f(v)
	
def print_twice(y):
	print y

print 'EXERCISE 3.4, PROBLEM 2,3, and 4:'	
do_twice(print_twice, 'spam')
print

#5. Define a new function called do_four that takes a function object and a value and calls the function four times, 
#passing the value as a parameter. There should be only two statements in the body of this function, not four.

def do_deux(f,v):
	f(v)
	f(v)
	
def print_deux(y):
	print y
	
def do_four(func,val):
	do_deux(func,val)
	do_deux(func,val)
	
print 'EXERCISE 3.4, PROBLEM 5:'
do_four(print_deux, 'Four prints from two statements - function calling function!')
print

#Exercise 3.5. This exercise can be done using only the statements and other features we have learned so far.
#1. Write a function that draws a grid like the following:
def draw_twoRow_grid():
	draw_oneRow_twoCells_head()
	draw_oneRow_twoCells_head()
	draw_horizontal_border()      #close out the last row of cells with a bottom border - To avoid OBOE (fencepost problem)
	
def draw_oneRow_twoCells_head():
	draw_horizontal_border()
	draw_vertical_borders()
	
def draw_horizontal_border():
	print '+', '- ' *4, '+', '- ' *4, '+'

def draw_vertical_borders():
	print '|', ' ' *8, '|', ' '*8, '|'
	print '|', ' ' *8, '|', ' '*8, '|'
	print '|', ' ' *8, '|', ' '*8, '|'
	print '|', ' ' *8, '|', ' '*8, '|'
	
print 'EXERCISE 3.5, PROBLEM 1:'
print 'Here is the grid with row rows and two columns:'
draw_twoRow_grid()
print
	
#2. Write a function that draws a similar grid with four rows and four columns.

print

def draw_fourRow_fourCols_grid():
	draw_oneRow_fourCells_head()
	draw_oneRow_fourCells_head()
	draw_oneRow_fourCells_head()
	draw_oneRow_fourCells_head()
	draw_hrzl_border()
	
def draw_oneRow_fourCells_head():
		draw_hrzl_border()
		draw_vert_borders()
		
def draw_hrzl_border():
		print '+', '- ' *4, '+', '- ' *4, '+', '- ' *4, '+', '- ' *4, '+'

def draw_vert_borders():
		print '|', ' ' *8, '|', ' '*8, '|', ' ' *8, '|', ' '*8, '|'
		print '|', ' ' *8, '|', ' '*8, '|', ' ' *8, '|', ' '*8, '|'
		print '|', ' ' *8, '|', ' '*8, '|', ' ' *8, '|', ' '*8, '|'
		print '|', ' ' *8, '|', ' '*8, '|', ' ' *8, '|', ' '*8, '|'

print 'EXERCISE 3.5, PROBLEM 2:'
print 'Here is the grid with four rows and four columns:'		
draw_fourRow_fourCols_grid()
print 
	