Python 3.11.5 (tags/v3.11.5:cce6ba9, Aug 24 2023, 14:38:34) [MSC v.1936 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#Strings
#When programming, we usually call text a string.  Think of a string as a collection of letters.  All the letters, numbers, and symbols could be a string, and so could our name and address.

#For example, lets take our Fred variable and use it to label a string:
Fred = "Why do gorillas have big nostrils? Big fingers?"
print Fred
SyntaxError: incomplete input
print (Fred)
Why do gorillas have big nostrils? Big fingers?

#You can also use single quotes to create a string
Fred = 'What is pink and fluffy?'
print (Fred)
What is pink and fluffy?

#However, if you try to enter more then one line of text for your string using only a single (') or double quote (") or if you start with one type of quote and finish with another, you will get an error message in the Python Shell

Fred = "What is pink and fluffy?'
SyntaxError: incomplete input

#This is and error message complaining about syntax because you did not follow the rules for ending a string with the same quote that you started with. Syntax means the arrangement and order of words in a sentence or, in this case the arrangement and order of words and symbols in a program.  So SyntaxError means that you did something in an order Python was not expecting, or Pyton was expecting something that you missed. EOL means end-of-line, so the rest of the error message is telling you that Python hit the end of the line and did not find a double quote to close (or finish) the string.
>>> 
>>> #To use more then one line of text in your string (called a multiline string), use three single quotes (''') and then hit ENTER between lines, like this:
>>> 
>>> Fred = '''How do dinosaurs pay their bills?
... With tryannosaurus checks!'''
>>> 
>>> #Lets print Fred to see if it worked.
>>> print (Fred)
How do dinosaurs pay their bills?
With tryannosaurus checks!
>>> 
>>> #The single and double quotes can become a problem when you are using words like Aren't, can't, shouldn't and wouldn't.  In order to solve this, use the tripple single quote (''') like we did with the double line.
>>> 
>>> silly_string = '''He said, "Aren't can't shouldn't wouldn't."'''
>>> print (silly_string)
He said, "Aren't can't shouldn't wouldn't."
>>> #If you really want to use single or double quotes to surround a string in Python, instead of three single quotes, you can add a backslash (\) before each quotationmark within a string.  This is called escaping. It is a way of telling Python that "Yes I know I have quotes inside my string, and I want you to ignore them until you see the end quote."  Escaping string can make them harder to read, so it's considered better practice to use multiline strings.  Still, you might come across code that uses escaping, so it's helpful to know why the backslashes are there.
>>> single_quote_str = 'He said, "Aren\'t can\'t shouldn\'t wouldn\'t"'
>>> double_quote_str = "He said, \"Aren't can't shouldn't wouldn't.\""
>>> print (single_quote_str)
He said, "Aren't can't shouldn't wouldn't"
>>> print (double_quote_str)
He said, "Aren't can't shouldn't wouldn't."
>>> 
>>> #If you want to display a message using the ontents of a variable, you can embed it in a special string, called and f-string (also known as a formatted string literal).  You put braces around the variable name, which will then be replaced by the actual value. (Embedding values, also referred to s string substitution, is programmer-speak for "inserting values.") For example, to have Python calculate or store the number of points you scored in a game, and then add it to a sentence like "I scored 10 points," and an f before the first quote and then replace the number 10 with the variable surrounded by the braces {}, like this:
>>> myscore = 1000
>>> message = f'Iscored {myscore} points'
>>> print (message)
Iscored 1000 points
>>> #We can also use more than one variable in a string:
>>> first = 0
>>> second = 8
>>> print (f"What did the number {first} say to number {second}? Nice belt!")
What did the number 0 say to number 8? Nice belt!
>>> 
>>> #We can even put expressions in an f-string like this:
>>> print (f'Two plus two equals {2+2}')
Two plus two equals 4
>>> #In this example, Pythonevaluates the simple equations between the braces, so the printed string contains the result.
