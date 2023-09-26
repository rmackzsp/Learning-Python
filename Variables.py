Python 3.11.5 (tags/v3.11.5:cce6ba9, Aug 24 2023, 14:38:34) [MSC v.1936 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
# Variables are like labels

#Variables in programming describes a place to store information such as numbers, text, lists of numbers and text and so on. For example, to create a variable name Fred, we use an equal sign (=)and then tell Python what information the variable should be the label for.
>>> 
>>> Fred = 100
>>> 
>>> #To find the value of a variable, enter print in the Python Shell, followed by the bariable name in parentheses.
>>> 
>>> print (Fred)
100
>>> 
>>> #We can also tell Python to change the variable Fred so that it labels something else. For example, here's how to change Fred to the number 200:
>>> Fred = 200
>>> print (Fred)
200
>>> 
>>> #On the first line, we say that Fred labels a number 200.  In the second line, we print the value of Fred, just to confirm the change.  Python prints the result on the last line.
>>> #We can also use more than one variable for the same item.
>>> Fred = 200
>>> John = Fred
>>> print (John)
200
>>> #Remember our equation for figuring out how many coins you would have at the end of the year if you could magially create new coins with your Grandfather's invention? We had this equation.
>>> 20+10*365
3670
>>> 3*52
156
>>> 3670-156
3514
>>> 
>>> #We can turn that into a single line of code:
>>> 20+10*365-3*52
3514
>>> 
>>> #That is not very easy to read, but what if we turn the numbers into variables?Try entering the following:
>>> found_coins = 20
>>> magic_coins = 10
>>> stolen_coins = 3
>>> 
>>> #The enteries create the variables found_coins, magic_coins, and stolen_coins.  Now, we can reenter the equation like this:
>>> found_coins + magic_coins * 365 - stolen_coins * 52
3514
>>> 
>>> #When we use a variable, we can simply change the varable to hold a new number and it will change everywhere it is used in the equation.
>>> stolen_coins = 2
>>> 
>>> found_coins + magic_coins * 365 - stolen_coins * 52
3566
