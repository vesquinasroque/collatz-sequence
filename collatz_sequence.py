players_number = None
global_number = None

def collatz(number):
    
    if number % 2 == 0:
        print(f"{number}", end=' ')
        return number // 2
    global global_number
    global_number = number
    else:
        print(f"{number}", end=' ')
        return 3 * number + 1
    global global_number
    global_number = number

while True:
    while players_number == None:
        try:
            print(f"Type a number:")
            players_number = int(input('>'))
        except ValueError:
            print (f"Please enter an integer")
            continue
    collatz(players_number)
    
    if global_number == 1:
        break
    else:
        collatz(global_number)


        

        