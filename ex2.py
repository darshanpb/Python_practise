# -*- coding: utf-8 -*-
''' 
Comma Code
Say you have a list value like this:
spam = ['apples', 'bananas', 'tofu', 'cats']
Write a function that takes a list value as an argument and returns
a string with all the items separated by a comma and a space, with and
inserted before the last item. For example, passing the previous spam list to
the function would return 'apples, bananas, tofu, and cats'. But your function
should be able to work with any list value passed to it. '''
import sys
def comma_code(parameter_list):
    string = str(parameter_list[0])
    for i in range(1,len(parameter_list)):
        string += (", "+str(parameter_list[i]))
    return string
if __name__ == "__main__":
    #spam = ['apples', 'bananas', 'tofu', 'cats']       #default values
    try:
        spam = list(input("List as a input to see output\n"))
    except (NameError,ValueError,TypeError) as identifier:
        print("Error occured try again with correct input")
        sys.exit()
    out = comma_code(spam)
    print(out)
