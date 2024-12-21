import art

def add(n1, n2):
    """Adds two numbers together"""
    return n1 + n2

def subtract(n1, n2):
    """Subtracts two numbers"""
    return n1 - n2

def multiply(n1, n2):
    """Multiplies two numbers"""
    return n1 * n2

def divide(n1, n2):
    """Divides two numbers"""
    return n1 / n2

operators = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide
}

def calculate(n1, n2, operation):
    """Takes two numbers and performs an operation on them according to the operations dictionary"""
    if operation not in operators:
        print("Invalid Input")
        return
    for o in operators:
        if o == operation:
            chosen_operation = operators[o]
            return chosen_operation(n1, n2)

print(art.logo)
in_use = True
keep_going = "different"
first_number = 0

while in_use:
    if keep_going == "different":
        first_number = int(input("which number would you like first? \n"))
    operator = input("which operation would you like to choose?\n")
    second_number = int(input("which number would you like second? \n"))
    result = calculate(first_number, second_number, operator)

    print(f"Your result so far is: {result}")

    safety_check = True
    while safety_check:
        keep_going = input("Would you like to keep going with the same number? Please type: same, different or quit.\n")
        if keep_going.lower() == "same":
            first_number = int(result)
            safety_check = False
        elif keep_going.lower() == "different":
            safety_check = False
        elif keep_going.lower() == "quit":
            in_use = False
            safety_check = False
        else:
            print("Invalid Input")
