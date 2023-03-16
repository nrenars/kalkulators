def text():
    print('\nChoose operator')
    print('Type 1 for "+" ')
    print('Type 2 for "-" ')
    print('Type 3 for "*" ')
    print('Type 4 for "/" ')
    print('Type 5 for "%" ')
    print('Type 0 to exit')


def add(x, y):
    return x + y

def  minus(x, y):
    return x - y

def multiply(x , y):
    return x * y

def devide(x, y):
    if y == 0:
        print('Can\'t devide by zero')
    else:
        return x / y
    
def percent(x):
    return x / 100

while True:
    text()
    choice = input('Your choice: ')

    if choice == '0':
        break
    
    num1 = float(input('Enter first number: '))

    if choice == '5':
        print((num1), '%', '=', percent(num1) )
        continue

    num2 = float(input('Enter second number: '))

    if choice == '1':
        print( int(num1), ' + ',  int(num2), ' = ', add(num1, num2))
    elif choice == '2':
        print( int(num1), '-', int(num2), '=', minus(num1, num2))
    elif choice == '3':
        print( int(num1), '*', int(num2), '=', multiply(num1, num2))
    elif choice == '4':
        print( int(num1), '/', int(num2), '=', devide(num1, num2))
    else:
        print('Invalid input, please try again')

