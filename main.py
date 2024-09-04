import random

max_lines = 3
max_bet = 100
min_bet = 1

rows = 3
cols = 3

symbol_count = {
    "A" : 2,
    "B" : 4,
    "C" : 6,
    "D" : 8 
}

symbol_value = {
    "A" : 5,
    "B" : 4,
    "C" : 3,
    "D" : 2 
}

def check_winnings(columns, lines, bet, values ):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check =  column[line]
            if symbol != symbol_to_check:
                break 
        else:
             winnings += values[symbol] * bet
             winning_lines.append(line + 1)
    return winnings, winning_lines




def get_slot_machine_spin(rows, cols, symbols ):
    all_symbols = []
    for symbol,symbol_count in symbols.items():
        for _ in range(symbol_count):
             all_symbols.append(symbol)

    columns =[]
    for _ in range(cols):
        column=[]
        current_symbols = all_symbols[:] 
        for _ in range(rows):
            value = random.choice(current_symbols )
            current_symbols.remove(value)
            column.append(value)
        columns.append(column)
    return columns 

def print_slot_machine(columns):
    for row in range( len(columns[0])):
        for i, column in enumerate (columns): 
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row],end="")
        print( )

def deposit():
    while True:
        amount = input("What would you like deposit? $")
        if amount.isdigit():
            amount =  int(amount)
            if amount > 0:
                break
            else:
                print("Enter the amount greater than 0.")
        else:
            print("Please a Enter a Number!")

    return amount


def get_number_of_lines():
    while True:
        lines = input("Enter the number of lines to bet on (1-" +str(max_lines)+  ")? " )
        if lines.isdigit():
            lines = int(lines)
            if 1<= lines <= max_lines:
                break
            else:
                print("Enter the valid number of lines")
        else:
            print("Please a Enter a Number!")

    return lines


def get_bet():
    while True:
        amount = input("how much would you like to bet on each line  ? $" )
        if amount.isdigit():
            amount = int(amount)
            if min_bet<= amount <= max_bet:
                break
            else:
                print(f"Enter the valid bet between ${min_bet} - ${max_bet}.")
        else:
            print("Please a Enter a Number!")

    return amount

def spin(Balance):
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines
        if total_bet > Balance:
            print(f"You do not have enough to bet that amount, your current balance is : {Balance }")
        else:
            break 
    
    print(f"You are Betting ${bet} on {lines} lines. Total best is equal to: ${total_bet}")
    
    slots = get_slot_machine_spin(rows, cols, symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value )
    print(f"You Won ${winnings}. ")
    print(f"You won on :", *winning_lines)
    return winnings - total_bet

def main():
    Balance = deposit()
    while True:
        print(f"Current Balance is ${Balance}" )
        ans = input("Press enter to spin( q to quit )")
        if ans == "q":
            break
        Balance += spin(Balance)
    print(f"You Left With ${Balance}")
    



main()      