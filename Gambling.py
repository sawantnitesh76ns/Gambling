import random 

MAX_LINES = 3
MIN_BET = 1
MAX_BET = 10

ROWS = 3
COLS = 3

symbols_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 3
}

symbols_values = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}

def check_winings(columns, lines, bet, values):
    winning = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            current_symbol = column[line]
            if symbol != current_symbol:
                break
        else:
            winning += values[symbol]* bet
            winning_lines.append(line + 1)
    return winning, winning_lines


def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)
    
    columns = []

    for _ in range(cols):
        column = []
        current_symbol = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbol)
            current_symbol.remove(value)
            column.append(value)
        columns.append(column)
    print(columns)
    return columns


def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")
        print()


def deposit():
    while True:
        amount = input("Please eneter the aount you would like to deposite $ ")
        if amount.isdigit():
            amount = int(amount)
            if int(amount) > 0:
                break
            else:
                print("Amount should be greater than 0")
        else:
            print("Please enter correct amount")
    return amount

def get_lines():
    while True:
        lines = input("Please eneter number f lines on which you would like to bet between (1 -" + str(MAX_LINES) +" ): ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Not valid number of lines")
        else:
            print("Please enter line betwen 1 to " + str(MAX_LINES))
    return lines

def get_bet():
    while True:
        bet = input("How much you would like to bet on each line $")
        if bet.isdigit() :
            bet = int(bet)
            if MIN_BET <= bet <= MAX_BET:
                break
            else:
                print("Bet amount should be between " + str(MIN_BET) + "-" + str(MAX_BET) )
        else:
            print("Bet amount should be between " + str(MIN_BET) + "-" + str(MAX_BET) )
    return bet

def spin(balance):
    lines = get_lines()
    while True:
        bet = get_bet()
        betAmount = bet * lines
        if betAmount > balance:
            print(f"You do not have enough bet amount, you current balance amount is ${balance}")
        else:
            print(f"You have betted ${bet} on ${lines} lines, so your total bet is ${betAmount}")
            break
    slots = get_slot_machine_spin(ROWS, COLS, symbols_count)
    print_slot_machine(slots)
    (winnigs, winning_lines) = check_winings(slots, lines, bet, symbols_values)
    print(f"Whore!!!! You won ${winnigs}")
    print(f"You won on", *winning_lines)
    return winnigs - betAmount

def main():
    balance = deposit()
    while True:
        print(f"Currnt Balance is ${balance}")
        answer = input("Please enter to play (q to quit).")
        if answer == "q":
            break
        else:
            balance += spin(balance)
    print(f"you left with ${balance}")


main()  