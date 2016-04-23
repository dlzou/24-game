import calc_24
import list_funcs

print("WELCOME TO THE 24 GAME")
while True:
    print("\n1. New calculation\n2. Quit")
    choice = input("Enter 1 or 2: ")
    if choice == '1':
        expressions = input("Enter 4 integers (a,b,c,d): ").replace(' ', '').split(',')
        numbers = []
        try:
            for n in range(0, len(expressions)):
                numbers.append(int(expressions[n]))
        except:
            pass
        if len(numbers) == 4:
            for n in range(4):
                numbers = list_funcs.rotate(numbers, 1)
                expressions = list_funcs.rotate(expressions, 1)
                calc_24.calculate(numbers, expressions, 4)

            c = calc_24.count
            user_input = ', '.join(str(n) for n in numbers)
            print("There are {} solutions for {}".format(c, user_input))
            calc_24.reset()
        else:
            print("4 integers required")
            pass
    elif choice == '2':
        print("THANKS FOR PLAYING")
        break
    else:
        print("Invalid entry")
        pass
