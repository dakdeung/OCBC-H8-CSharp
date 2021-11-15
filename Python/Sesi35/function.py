def get_personal_info(name, age):
    print('Name:', name)
    print('Age:', age)

get_personal_info('ani', 27)

get_personal_info(age=35,name='aku')

def buy(name, *items):
    print(name, items)

buy('roy', 'chocolate bar')
buy('tia', 'eggs', 'wheat', 'float', 'chocolate bar')

# -*- coding: utf-8 -*-
"""
## Python Function

A function is a block of organized, **reusable code** that is used to perform a single, related action. Functions provide better modularity for your application and a high degree of code reusing.

As you already know, Python gives you many built-in functions like `print()`, etc. but you can also create your own functions. These functions are called user-defined functions.

### Defining a Function

You can define functions to provide the required functionality. Here are simple rules to define a function in Python.

* Function blocks begin with the keyword `def` followed by the function name and parentheses ( `( )` ).
* Any input parameters or arguments should be placed within these parentheses. You can also define parameters inside these parentheses.
* The first statement of a function can be an optional statement - the documentation string of the function or docstring.
* The code block within every function starts with a colon (`:`) and is indented.
* The statement return `[expression]` exits a function, optionally passing back an expression to the caller. A return statement with no arguments is the same as return None.

```
def function_name( parameters ):
   '''docstring'''
   statement(s)
```

By default, parameters have a positional behavior and you need to inform them in the same order that they were defined.

The first string after the function header is called the docstring and is short for documentation string. It is used to explain in brief, what a function does.

Although optional, documentation is a good programming practice. Unless you can remember what you had for dinner last week, always document your code.

In the above example, we have a docstring immediately below the function header. We generally use triple quotes so that docstring can extend up to multiple lines. This string is available to us as `__doc__` attribute of the function.
"""

# Example of Function Creation

def my_function(p, l):
    '''Function to calculate area of a square'''
    print(p * l)


def printme( str_input ):
   '''This prints a passed string into this function'''
   print(str_input)



"""### Calling a Function

Defining a function only gives it a name, specifies the parameters that are to be included in the function and structures the blocks of code. Once the basic structure of a function is finalized, you can execute it by calling it from another function or directly from the Python prompt. The code below is the example to call `printme()` function.
"""

# Function definition is here
def printme( str_input ):
   '''This prints a passed string into this function'''
   print(str_input)

# Now you can call printme function
printme("I'm first call to user defined function!")
printme("Again second call to the same function")

"""### Pass by reference vs value

All parameters (arguments) in the Python language are passed by reference. It means if you change what a parameter refers to within a function, the change also reflects back in the calling function. For example 
"""

# Function definition is here
def changeme( mylist ):
   '''This changes a passed list into this function'''
   mylist = mylist+[1,2,3,4]
   print("\nValues inside the function : ", mylist)
   return mylist

# Now you can call changeme function
mylist = [10,20,30]
print("\nValues outside the function - before : ", mylist)
mylist = changeme( mylist )
print("\nValues outside the function - after  : ", mylist)

"""There is one more example where argument is being passed by reference and the reference is being overwritten inside the called function."""

# Function definition is here
def changeme( mylist ):
   '''This changes a passed list into this function'''
   mylist = [1, 2, 3, 4] # This would assign new reference in mylist
   print("Values inside the function  : ", mylist)

# Now you can call changeme function
mylist = [10, 20, 30]
changeme( mylist )
print("Values outside the function : ", mylist)

"""### Function Arguments

You can call a function by using the following types of formal arguments −

- Required arguments
- Keyword arguments
- Default arguments
- Variable-length arguments

#### **Required arguments**

Required arguments are the arguments passed to a function in **correct positional order**. Here, the number of arguments in the function call should match exactly with the function definition.

To call the function `printme()`, you definitely need to pass one argument, otherwise it gives a syntax error as follows.
"""

# Function definition is here
def printme( str_input ):
   '''This prints a passed string into this function'''
   print(str_input)
 
# Now you can call printme function
printme("Hello")

# # This syntax will give you an error
# printme()

"""One more example of required arguments. Let's create function that can calculate area of rectangle."""

# Function definition is here
def calculate_rect(length, width):
  '''This function is used to calculate area of rectangle'''
  print('Area : ', length*width)

# Define parameters
length = 100
width = 20

# Call calculate_rect
calculate_rect(length, width)

# # This syntax will give you an error
# calculate_rect(length)

"""#### **Keyword Arguments**

Keyword arguments are related to the function calls. When you use keyword arguments in a function call, the caller **identifies the arguments by the parameter name**.

This allows you to **skip arguments or place them out of order** because the Python interpreter is able to use the keywords provided to match the values with parameters. You can also make keyword calls to the `printme()` function in the following ways.

"""

# Function definition is here
def printme( str_input ):
   '''This prints a passed string into this function'''
   print(str_input)

# Now you can call printme function
printme(str_input = "Hacktiv8")

"""The following example gives more clear picture. Note that the order of parameters does not matter."""

# Function definition is here
def printinfo( name, age ):
   '''This prints a passed info into this function'''
   print("Name : ", name)
   print("Age. : ", age)

# Now you can call printinfo function
printinfo( age=4, name="a" )

"""#### **Default Arguments**

A default argument is an argument that **assumes a default value if a value is not provided** in the function call for that argument. The following example gives an idea on default arguments, it prints default `age` if it is not passed.
"""

# Function definition is here
def printinfo( name, age = 26 ):
   '''This prints a passed info into this function'''
   print("Name : ", name)
   print("Age  : ", age)
   print("")

# Now you can call printinfo function
printinfo( age=50, name="hacktiv8" )
printinfo( name="hacktiv" )

"""You must write default-arguments **after** required-argument

Example : 
> `def printinfo(name, age=26):`

NOT 
> `def printinfo(age=26, name):`
"""

# Function definition is here
def printinfo( name, age = 26 ):
   '''This prints a passed info into this function'''
   print("Name : ", name)
   print("Age  : ", age)
   print("")

# Now you can call printinfo function
printinfo( age=50, name="hacktiv8" )

# # Function definition is here
# def printinfo( age = 26, name ):
#    '''This prints a passed info into this function'''
#    print("Name : ", name)
#    print("Age  : ", age)
#    print("")

# # Now you can call printinfo function
# printinfo( age=50, name="hacktiv8" )

"""#### **Variable-length Arguments**

You may need to process a function for **more arguments than you specified** while defining the function. These arguments are called variable-length arguments and are not named in the function definition, unlike required and default arguments.

Syntax for a function with non-keyword variable arguments is this −

```py
def functionname(args, *var_args_tuple ):
   '''function_docstring'''
   function_suite
   return [expression]
```

An asterisk (`*`) is placed before the variable name that holds the values of all nonkeyword variable arguments. All variable values in an asterisk, will be saved into a `tuple`. This `tuple` remains empty if no additional arguments are specified during the function call. The code below is a simple example.
"""

# Function definition is here
def printinfo( arg1, *vartuple ):
# def printinfo(arg1, arg2, arg3, arg4):
   '''This prints a variable passed arguments'''
   print('arg1     : ', arg1)
   print('vartuple : ', vartuple)
   print('')
   
   for var in vartuple:
      print('isi vartuple : ', var) 

# Now you can call printinfo function
printinfo( 10 )
printinfo( 70, 60, 50, "a" )

"""Variable-length Argument have two types.

* `*` : All nonkeyword variables will be saved in a `tuple`.
```py
def functionname(args, *var_args_tuple ):
   '''function_docstring'''
   function_suite
   return [expression]
```

* `**` : All nonkeyword variables will be saved in a `dict`.
```py
def functionname(args, **var_args_dict ):
   '''function_docstring'''
   function_suite
   return [expression]
```
"""

# Create a function with nonkeyword variables

def person_car(total_data, **kwargs):
  '''Create a function to print who owns what car'''
  print('Total Data : ', total_data)
  for key, value in kwargs.items():
    print('Person : ', key)
    print('Car    : ', value)
    print('')

person_car(3, jimmy='chevrolet', frank='ford', tina='honda')
person_car(3)

# Parameters (jimmy='chevrolet', frank='ford', tina='honda') will be equal to
# kwargs = {
#     'jimmy': 'chevrolet',
#     'frank': 'ford',
#     'tina': 'honda'
# }

"""### The Anonymous Functions

These functions are called anonymous because they are not declared in the standard manner by using the `def` keyword. You can use the `lambda` keyword to create small anonymous functions.

- `lambda` forms can take any number of arguments but return just one value in the form of an expression. They cannot contain commands or multiple expressions.
- An anonymous function cannot be a direct call to `print` because `lambda` requires an expression
- `lambda` functions have their own local namespace and cannot access variables other than those in their parameter list and those in the global namespace.

The syntax of `lambda` functions contains only a single statement, which is as follows −

`lambda [arg1 [,arg2,.....argn]]:expression`

The code below is the example to show how `lambda` form of function works.
"""

# Function definition is here
sum = lambda arg1, arg2: arg1 + arg2

# That lambda function will be equal to :
# def sum(arg1, arg2):
#     return arg1+arg2

# Now you can call sum as a function
print("Value of total : ", sum( 10, 20 ))
print("Value of total : ", sum( 20, 20 ))

"""### The `return` Statement

The statement `return [expression]` exits a function, optionally passing back an `expression` to the caller. A `return` statement with no arguments is the same as `return None`.

All the above examples are not returning any value. You can return a value from a function as follows.
"""

# Function definition is here
def sum(arg1, arg2):
    # Add both the parameters and return them."
    total = arg1 + arg2
    return total

# Now you can call sum function
total = sum(10, 20)
print("Result function : ", total)

"""### Scope of Variables

All variables in a program may not be accessible at all locations in that program. This depends on where you have declared a variable.

The scope of a variable determines the portion of the program where you can access a particular identifier. There are two basic scopes of variables in Python

- Global variables
- Local variables

**Global vs. Local variables**

Variables that are defined inside a function body have a local scope, and those defined outside have a global scope.

This means that local variables can be accessed only inside the function in which they are declared, whereas global variables can be accessed throughout the program body by all functions. When you call a function, the variables declared inside it are brought into scope.
"""

# Declare a global variable
total = 0

# Create sum function
def sum( arg1, arg2 ):
   total = arg1 + arg2; 
   print("Inside the function local total   : ", total)

# Call a function
sum( 10, 20 )
print("Outside the function global total : ", total)

"""Let's check effect of `return` statement to the above code and pass it into the same-name variable. We will see that variable `total` has changed in global scope."""

# Declare a global variable
total = 0

# Create sum function
def sum( arg1, arg2 ):
   total = arg1 + arg2; 
   print("Inside the function local total   : ", total)
   return total

# Call a function
print("Outside the function global total - before : ", total)
total = sum( 10, 20 )
print("Outside the function global total - after  : ", total)

"""### Docstring

A docstring is a string literal that occurs as the first statement in a module, function, class, or method definition. Such a docstring becomes the `__doc__` special attribute of that object.

All modules should normally have docstrings, and all functions and classes exported by a module should also have docstrings. 

For consistency, always use '''triple single quotes''' or '''triple double-quotes''' around docstrings.

There is no strict rules how to write the docstring. You can write the docstring as you like. For clear explanation, Docstring usually contains 3 parts :
* Aims of a module, function, class, or method.
* Description of input parameter with their types.
* Description of output parameter (only if return something).
"""

# Example of docstring in a function

def sum_number(num1, num2):
  '''
  This function is used to sum of 2 variables.
  :param num1: Input number 1 | int or float
  :param num2: Input number 2 | int or float
  
  :return: num3: Sum of number | int or float
  '''

  num3 = num1 + num2
  return num3

# Syntax to get explanation/docstring from a particular module/function/class

print(sum_number.__doc__)
