#Questions from Pierian Data
#These are my solutions

#Q1: Use for, .split(), and if to create a Statement that will print out words that start with 's':

st = 'Print only the words that start with s in this sentence'
for word in st.split():
    if word[0].lower() == 's':
        print(word)

#Q2: Use range() to print all the even numbers from 0 to 10.

for i in range(0,11,2):
    print(i)

#Q3: Use a List Comprehension to create a list of all numbers between 1 and 50 that are divisible by 3.

number_theory = [x for x in range (1,51) if x%3 ==0]
print(number_theory)

#Q4: Go through the string below and if the length of a word is even print "even!"

ct = 'Print every word in this sentence that has an even number of letters'
for even in ct.split():
    if len(even) % 2 == 0:
        print(even + " is even!")

#Q5: Write a program that prints the integers from 1 to 100. But for multiples of three print "Fizz" instead of the number, and for the multiples of five print "Buzz". For numbers which are multiples of both three and five print "FizzBuzz".

for i in range(1,101):
    if num % 15 == 0:
        print('FizzBuzz')
    
    elif num % 3 == 0:
        print('Fizz')
    
    elif num % 5==0:
        print('Buzz')
    
    else:
        print(i)

#Q6: Use List Comprehension to create a list of the first letters of every word in the string below:

dt = 'Create a list of the first letters of every word in this string'
magic = [word[0] for word in st.split()]
