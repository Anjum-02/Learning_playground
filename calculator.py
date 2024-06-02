def addition(input_values):
    result = 0
    for i in input_values:
        result = result + i
    print("The result of the ADDITION is: ",result)


def subtraction(input_values):
    result = 0
    for i in input_values:
        result = i - result
    print("The result of the SUBTRACTION is:", result)


def multiplication(input_values):
    result = 1
    for i in input_values:
        result = result * i
    print("The result of the MULTIPLICATION is:", result)


def division(A, B):
    result = A // B
    print("The result of the Quotient is:", result)
    reminder = A % B
    print("The result of the Reminder is:", reminder)



while True:
    select_oper=(input("select the operation to perform \n 1 ADD 2 SUB, 3.MULTI, 4 DIV, 5.EXIT:"))
    if select_oper == 'EXIT':
        break
    input_values = []

    if select_oper =="DIV":
       result=1
       A=int(input("Enter the DIVISOR value"))
       B=int(input("enter the DIVIDENT value"))
       division(A, B)
    else:
        while True:
            try:
                values = int(input("Enter the number"))
                input_values.append(values)
            except: break
        print(input_values)

        if select_oper == "ADD":
            addition(input_values)

        elif select_oper == "SUB":
            subtraction(input_values)

        elif select_oper == "MULTI":
            multiplication(input_values)



