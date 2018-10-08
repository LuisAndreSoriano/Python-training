#####learnpython.org #####

### Hello, World
print("This line will be printed.")

### Indentation
x = 1
if x == 1:
    print("x is 1.") # indented four spaces

    # NOTE!!! INDENT IS PART OF PYTHON SYNTAX
    
### Variables and Types
    # Python is object oriented.
    # You do not need to declare variables before using them

### Numbers
    
# integers
myint = 7
print(myint)

# floating point numbers
myfloat = 7.0
print(myfloat)
myfloat = float(7)
print(myfloat)

# samples of calculations

print(2+2) # Python supports + - * /
print(8/5) # division always return floating number
print(8//5) # floor function
print(8%5) # returns the remainer
print(1j+1j) # returns complex number, in this case, imaginary prefixed by n

### Strings

# Examples

# literals...
print("Hello")
print("Don't worry about apostrophes")
print (3*'un'+'wow') # to repeat multiple strings, use *

# masking...
print('"Isn\'t", they said.') # to escape some characters, use \
print(r'C:\Users\Luis') # to print literals, without escape

# concatenating...
print('Py' 'thon') # automatically concatenates
print('Put several strings within parentheses'
      'to have them joined together.') # ill return one line of string
Py = "Py"
print(Py + "thon") # use + to concatenate variable with another variable or literal

# indexing
word = "Python"
print(word[0]) # prints "P" as "P" is in position 0
print(word[5]) # arrays at Python start at 0!!!!!
print(word[-1]) # last character NEGATIVE INDEX START AT -1
print(word[-2]) # second-last character

# slicing (aka substrings)
print(word[0:2]) # characters from position 0 (included) to position 2 (excluded)
print(word[:2])
print(word[2:])
print(word[:2] + word[2:])
# this is so that word[:i]+word[i:] == word

# note: indexing out of range results to error but slicing wont

