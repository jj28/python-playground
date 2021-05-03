def print_calculated_advcon(value):
    print('ADVCON\'s TP: ' + str(float(value) * 1.2))


def check_int_float(userInput):
    try:
        # Convert userInput into INTEGER. ValueError will trigger of userInput is not INTEGER
        userInputToInt = int(userInput)
        print_calculated_advcon(userInputToInt)
    except ValueError:
        try:
            # Convert userInput into FLOAT. ValueError will trigger of userInput is not FLOAT
            userInputToFloat = float(userInput)
            print_calculated_advcon(userInputToFloat)
        except ValueError:
            print('Please enter valid Enter Price')


def practise_1():
    userInput = input("Enter Enter Price: ")
    check_int_float(userInput)


if __name__ == '__main__':
    practise_1()

