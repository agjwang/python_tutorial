import re

print("Calculator")
print("Type \'quit\' to quit")

previous = 0
run = True

def perform_math():
    global run
    global previous
    if previous == 0:
        equation = raw_input("Enter equation: ")
    else:
        equation = raw_input(str(previous))

    if equation == 'quit':
        run = False
    else:
        equation = re.sub('[a-zA-Z,.:()" "]', "", equation)
        
        if previous == 0:
            previous = eval(equation)
        else:
            previous = eval(str(previous) + equation)

while run:
    perform_math()