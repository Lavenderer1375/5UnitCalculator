def Calc():
    user_input1 = int(float(input("Add first Number\n")))
    user_input2 = int(float(input("Add second Number\n")))
    user_input3 = input("Add the Unit\n")
    resultext = "The answere is:\n"
    try:
        if user_input3 == "+":
            result = user_input1 + user_input2
            print(resultext, result)
        elif user_input3 == "-":
            result = user_input1 - user_input2
            print(resultext, result)
        elif user_input3 == "*":
            result = user_input1 * user_input2
            print(resultext, result)
        elif user_input3 == "/":
            result = user_input1 / user_input2
            print(resultext, result)
        elif user_input3 == "%":
            result = user_input1 % user_input2
            print(resultext, result)
        else:
            print("Use Units Only (+, -, *, /, %")
    except ValueError:
        print("Don't Enter Text!")

user_input = ""
while user_input != "Done":
    print("Welcome to Calc!\nTo Exit the programm type 'Done'")
    Calc()
