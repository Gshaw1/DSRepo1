
# coding: utf-8

# <img src="http://imgur.com/1ZcRyrc.png" style="float: left; margin: 20px; height: 55px">
# 
# # Project 1: Python Coding Exercises
# 
# _Authors: Joseph Nelson (DC)_
# 
# ---

# The following code challenges are drawn from common exercises used in technical interviews.
# 
# Please note that there may be several ways to approach each challenge. If you get stuck, try mapping out your approach in pseudocode first. Finally, while solutions to problems like these may be found online, remember that if you copy/paste code that you can't explain, you'll be missing out on the point of the project. The only way to truly learn a new skill is through practice, trial, and error - we can only help you improve by understanding where you are having trouble.

# ### Challenge 1: Largest Palindrome
# A palindromic number reads the same both ways. For example, 1234321 is a palindrome. The largest palindrome made from the product of two two-digit numbers is 9009 = 91 × 99. Find the largest palindrome made from the product of two three-digit numbers. Afterward, write a brief explanation walking through your code's logic in markdown.

# In[2]:


Product = 101
def CheckIFPalendrome(Product): #This Function Checks to see if a string is a palendrome
    PalendromeBool = True
    Product = str(Product) #convert datatype to string
    StrLen = len(Product) #find length of string
    for i in range(0, StrLen): #counter from first to last element
        if Product[0+i] == Product[StrLen-i-1]: #if first element + counter(i) = Last element - counter(i) then move to next element
            pass
        else:
            PalendromeBool = False #if above test fails string is not a palendrome

    return PalendromeBool

PalendromeList = [] #create a list to hold Palendromes

for NumRange1 in range(100,999): 
    for NumRange2 in range(100,999): #These nested loops will produce every combination of three digit numbers
        Product  = NumRange1 * NumRange2 #Find product of two numbers
        if CheckIFPalendrome(Product) == True: #Pass product through the function
            PalendromeList.append(Product) #if it is a palendrome add to list
            
print(max(PalendromeList)) #find and print max of list


# 
# ### Challenge 2: Summation of Primes
# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17. Find the sum of all the primes below 2,000. Afterward, write a brief explanation walking through your code's logic in markdown.

# In[33]:



def CheckIfPrime(Number): #This Function Checks to see if a number is prime

    NotPrime = True

    for DivideRange in range(2,Number): #Range of numbers that we will try too divide into number we are checking
        if Number % DivideRange == 0: #if a number divides into the test number with remainder 0 then it is not prime
            NotPrime = False #NotPrime Bool
            
    return NotPrime #Returns True or False Value

PrimeList = []

for PrimeRange in range(1,2000): #Loop through range of numbers from 1 to 2000
    if CheckIfPrime(PrimeRange) == True: #check to see if it is prime using function above
        PrimeList.append(PrimeRange) #add to list of prime numbers
        
TotalSum = sum(PrimeList) #sum all numbers in list
print(TotalSum) #print result


# ### Challenge 3: Multiples of 3 and 5
# If we list all of the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6, and 9. The sum of these multiples is 23. Find the sum of all the multiples of 3 and 5 below 1,000. Afterward, write a brief explanation walking through your code's logic in markdown.

# In[1]:


ThreeFiveMultList = []


for ThreeFiveMult in range(1,1000):
    if ThreeFiveMult % 3 == 0 or ThreeFiveMult % 5 == 0:
        ThreeFiveMultList.append(ThreeFiveMult)
        
#print(ThreeFiveMultList)
TotalSum = sum(ThreeFiveMultList)
print(TotalSum)


# ### Challenge 4: String Compressor
# Implement a method to perform basic string compression using the counts of repeated characters. (This is called run-length encoding.) For example, the string "aabcccccaaa" would become a2b1c5a3. If the “compressed” string would not become smaller than the original string, your method should return the original string. You can assume the string has only uppercase and lowercase letters (a–z). Specify whether your solution is case sensitive or case insensitive and what you would need to change to make it the other. Afterward, write a brief explanation walking through your code's logic in markdown.

# In[4]:


TestString = 'aabcccccaaa'

def ComppressString(InputString):
    PositionCount = 0
    CharCount = 0
    OutPutString = ''
    #for Element in InputString:
        
    for i in range(PositionCount, len(InputString)):

        if InputString[PositionCount] == InputString[i]:
            CharCount +=1
            print(InputString[PositionCount] + InputString[i] + str(CharCount))
        else:
            OutPutString += InputString[PositionCount]  + str(CharCount)
            #print(PositionCount)
            print(InputString[i] + 'else')
            CharCount == 0
            print(i)
            PositionCount += 1
    #print(OutPutString)
    return OutPutString

ComppressString(TestString)


# In[40]:


def compress(string):

    res = ""

    count = 1

    #Add in first character
    res += string[0]

    #Iterate through loop, skipping last one
    for i in range(len(string)-1):
        if(string[i] == string[i+1]):
            count+=1
        else:
            if(count > 1):
                #Ignore if no repeats
                res += str(count)
            res += string[i+1]
            count = 1
    #print last one
    if(count > 1):
        res += str(count)
    return res

TestString = 'aabcccccaaa'
compress(TestString)


# ### *BONUS* Challenge: FizzBuzz
# Write a program that prints all of the numbers from 1 to 100. For multiples of 3, instead of the number, print "Fizz;" for multiples of 5, print "Buzz." For numbers that are multiples of both 3 and 5, print "FizzBuzz." Afterward, write a brief explanation walking through your code's logic in markdown.

# In[27]:


for i in range(1,31):
    if i % 3 == 0 and i % 5 == 0:
        print('fizzbuzz')
    elif i % 5 == 0:
        print('buzz')
    elif i % 3 == 0:
        print('fizz')
    else:
        print(i)
print('Pointless string at end')

