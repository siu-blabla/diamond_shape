def diamond(n):
    # Check if the input is an odd integer, if not, return a message.
    if n % 2 == 0:
        return "Please provide an odd integer."
    # Loop to create the pattern
    for i in range(n):
        if i <= n // 2:
            print(' ' * (n // 2 - i) + '*' * (2 * i + 1))
        else:
            print(' ' * (i - n // 2) + '*' * (2 * (n - i) - 1))


# Loop to keep asking for user input until they decide to stop
while True:
    try:
        user_input = int(input("\033[93m\033[1mEnter an odd integer for the diamond size: \033[0m"))
        print("-------------------------------------------------------------")
        print()
        result = diamond(user_input)
        if result:
            print(result)
    # Handle the error when the input is not a valid integer.
    except ValueError:
        print()
        print("-------------------------------------------------------------")
        print("\033[91mInvalid input. Please enter an integer.\033[0m")
        print("-------------------------------------------------------------")
    # Loop to ask the user if they want to create another diamond.
    while True:
        print()
        print("-------------------------------------------------------------")
        another = input("Do you want to create another diamond? (y/n): ").strip().lower()
        print("-------------------------------------------------------------")
        # Break the loop if the input is valid ('y' or 'n')
        if another in ['y', 'n']:
            break
        # If the input is invalid, show an error message
        print("\033[91mInvalid input. Please enter 'y' or 'n'.\033[0m")
    # If the user doesn't want to create another diamond, exit the program
    if another != 'y':
        print("End of program. Thank you")
        break
