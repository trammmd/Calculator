def calculate():

    number_1 = int(input('First number: '))

    operator = input('Math operator: ')

    number_2 = int(input('Second number: '))

    if operator == '+':
        print("Your math calculation {} {} {} =".format(number_1, operator, number_2))
        print(number_1 + number_2)

    elif operator == '-':
        print("Your math calculation {} {} {} =".format(number_1, operator, number_2))
        print(number_1 - number_2)

    elif operator == '*':
        print("Your math calculation {} {} {} =".format(number_1, operator, number_2))
        print(number_1 * number_2)

    elif operator == '/':
        if number_2 == 0:
            print("Second value is 0")
        print("Your math calculation {} {} {} =".format(number_1, operator, number_2))
        print(number_1 / number_2)

    else:
        print('Operator is unvalid')

calculate()