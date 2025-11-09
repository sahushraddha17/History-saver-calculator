# STEP 1 -  CRETAE TXT HISTORY_FILE
HISTORY_FILE = "history.txt"
# STEP 2 - CRETAE FUNCTION TO SHOW HISTORY
def show_history():
    with open(HISTORY_FILE, 'r') as file:
        lines = file.readlines()
    if len(lines) == 0:
        print("NO HISTORY FOUND")
    else:
        for line in reversed(lines):
            print(line.strip())
# STEP 3 - CREATE FUNCTION TO CLEAR HISTORY
def clear_history():
    with open(HISTORY_FILE, 'w'):
        pass
    print("History cleared")
# STEP 4 - CREATE FUNCTION TO SAVE TO HISTORY
def save_to_history(equation, result):
    with open(HISTORY_FILE, 'a') as file:
        file.write(equation + ' = ' + str(result) + '\n')
# STEP 5 - CREATE CALCULATOR FUNCTION
def calculate(user_input):
    parts = user_input.split()
    if len(parts) != 3:
        print('Invalid input. Use format like: 2 + 3')
        return

    num0 = float(parts[0])
    op = parts[1]
    num2 = float(parts[2])

    if op == '+':
        result = num0 + num2
    elif op == '-':
        result = num0 - num2
    elif op == '*':
        result = num0 * num2
    elif op == '/':
        if num2 == 0:
            print("Error: Division by zero is not possible")
            return
        result = num0 / num2
    elif op == '%':
        if num2 == 0:
            print("Error: Division by zero is not possible")
            return
        result = num0 % num2
    elif op =='**':
        result = num0 ** num2    
    else:
        print('Invalid operator. Use only +, -, *, /', '%, **')
        return

    if int(result) == result:
        result = int(result)

    print("RESULT =", result)
    save_to_history(user_input, result)

# STEP - 6 - CREATE MAIN FUNCTION FOR USER INTERACTION
def main():
    print("Welcome to the calculator ('Show history', 'Clear istory', or 'Exit')")
    while True:
        user_input = input("Enter your equation with sapses like 2(space)+(space)3 (+, -, *, /, %, **): ")
        if user_input == "Exit":
            print("Exiting the calculator. Goodbye!")
            break
        elif user_input == " Show history":
            show_history()
        elif user_input == "Clear history":
            clear_history()
        else:
            calculate(user_input)

main()
