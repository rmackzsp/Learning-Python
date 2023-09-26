Python 3.11.5 (tags/v3.11.5:cce6ba9, Aug 24 2023, 14:38:34) [MSC v.1936 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
8*3.57
28.56

#Suppose you are digging in your backyard and uncover a bag of 20 gold coins. The next day you sneak down to the basement and stick the coins inside your Grandfather's steam powered replicating invention (luckily, you can just fit the 20 coins inside). You hear a whiz and a pop and, a few hours later, out shoot another 10 gleaming coins.  How many coins would you have if you did this every day for a year?

10*365
3650

#Plus the 20 you originally found

3650+20
3670

>>> # Now what if a Raven spots the shiny gold coins and every week flies off with 3 of them, how many would you have at the end of the year?
... 
>>> 3*52
156
>>> 
>>> # 156 is the number of coins that is stolen by the Raven every year. 
... 3670-156
3514
>>> 
>>> # Took the total of 3670 and subtracted the 156 that the Raven stole for a total remaining of 3514
... 
>>> #   Symbol      Operation
>>> #     +         Addition
>>> #     -         Subtraction
>>> #     *         Multiplication
>>> #     /         Division
>>> 
>>> # We use parentheses in programming languages to control the order of operations.  An poeration is anything that uses an operator.  Multiplication and division have a higher order than addition and subtraction, so thery're preformed first.
>>> 
>>> #For example, in the following equation, the numbers 30 and 20, are multiplied first, and then number 5 is added to their product:
>>> 5+30*20
605
>>> 
>>> #This equation is another way of saying, "Multiply 30 by 20, and then add 5 to the result." The result is 605. We can change the order of the operations by adding parentheses around the first two numbers, like so:
>>> (5+30)*20
700
>>> 
>>> #The result of this wquation is 700 (not 605) because the parentheses tells Python to do the operatioin in the parentheses first, and then do the operation outside the parentheses. This example is saying, "Add 5 to 30, and then multiply the result by 20."
>>> 
>>> #Parentheses can be nested, which means that there can be parentheses inside parentheses, like this:
>>> ((5+30)*20)/10
70.0
>>> 
>>> #In this case, Python evaluates the innermost parentheses first, then the outer ones, and then the final division operator. In other words, this equation is saying,
>>> #"Add 5 to 30, then multiply the result by 20, and divide that result by 10." Here's what happens:
>>> #1. Adding 5 to 30 gives you 35
>>> #2. Multiplying 35 by 20 gives 700.
>>> #3. Dividing 700 by 10 gives the final answer of 70.
>>> 
>>> #If we had not used parentheses, the result would be slightly different:
>>> 5+30*20/10
65.0
>>> 
