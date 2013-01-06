# Exercises for chapter 2: Problems 2.1, 2.2, 2.3, and 2.4 in Think Python

# Name: Sidd Tewari

# Chapter 2: Problems 2.1, 2.2, 2.3, and 2.4. 
# If the question asks for a response, instead of writing code, just write your text in a comment (use # to begin a comment) - 
# WHERE POSSIBLE, I changed the answer comments to print statements

#------------------------------------------------------------------------------------------------------------------------------------
# 2.1 - Zip Code - Can you figure out what is going on? Hint: display the values 01, 010, 0100 and 01000.
print
print 'EXERCISE 2.1:'
print 'When typing an integer with a leading value of zero, the interpreter seems to be interpreting it with different bases like Base 2 for 01, Base 3 for 010'
print
#------------------------------------------------------------------------------------------------------------------------------------
# 2.2 - ... Now put the same statements into a script and run it. What is the output? 
# Modify the script by transforming each expression into a print statement and then run it again.

print 'EXERCISE 2.2:'
print 5
x = 5
print 'x+1 = ', (x + 1), '   ', '(where x = 5)'
print
#------------------------------------------------------------------------------------------------------------------------------------
# 2.3  width = 17
# height = 12.0
#delimiter = '.'

#Answers
print 'EXERCISE 2.3:'
print '1. width/2 = 8 (floor division) in Python 2; should be 8.5 in Python 3'
print '2. width/2.0 = 8.5'
print '3. height/3 = 4.0'
print '4. 1 + 2 * 5 = 11'
print "5. delimiter * 5 = '.....'"
print
#------------------------------------------------------------------------------------------------------------------------------------

# 2.4    
    
# 1. Area of the sphere
pi = 3.1415926535897932
area = ((4.0/3.0)*(pi)*(5**3)) #using float 4.0/3.0 instead of integer to accomodate for the python interpreter's floor division and to get the accurate value of 4/3
print 'EXERCISE 2.4:'
print 'Area of the sphere is: ', area
print

# 2. Suppose the cover price of a book is $24.95, but bookstores get a 40% discount. 
#Shipping costs $3 for the first copy and 75 cents for each additional copy. What is the total wholesale cost for 60 copies?
cost = 24.95
discount = 40.0
discountedCost = cost - ((discount/100)*cost)      #Additional test step - print discountedCost

oneShipCost = 3.0
addShipCost = 0.75

n = 60.0   #Where n is the number of units to be sold

totalShipCost = (oneShipCost + (addShipCost*(n-1.0)))
wholesaleCost = ((discountedCost*n) + (totalShipCost))
print 'EXERCISE 2.4:'
print 'The wholesaleCost for 60 books is:', wholesaleCost
print 

# 3. If I leave my house at 6:52 am and run 1 mile at an easy pace (8:15 per mile), then 3 miles at tempo (7:12 per mile) 
# and 1 mile at easy pace again, what time do I get home for breakfast?

startTime = ((6*60)+52) * 60 # starting time, 06:52:00 am, in seconds

easyPace = ((8*60)+15)  #easy pace of 00:08:15 per mile - in seconds
tempoPace = ((7*60)+12) #tempo pace of 00:07:12 per mile - in seconds

runTime = (easyPace*1) + (tempoPace*3) + (easyPace*1) #total seconds taken for the five miles run at two different paces

endTime = startTime + runTime #endTime in seconds

endHr = endTime/(60*60) 
endMin = (endTime%(60*60)) / 60

print 'EXERCISE 3:'
print ('The runner returns for breakfast at ' + str(endHr) + ':' + str(endMin))
print
