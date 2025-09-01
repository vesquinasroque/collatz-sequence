players_number = None

def collatz(number):
    
    if number % 2 == 0:
        return number // 2
    return 3 * number + 1

while True:
    while players_number == None:

        try:
            print(f"Type a number:")
            players_number = int(input('>'))

        except ValueError:
            print (f"Please enter an integer")
            continue
    
        result = collatz(players_number)

    if result == 1:
        break
    else:
        result = collatz(result)
    
    print(f"{result}", end =' ')


        

        
