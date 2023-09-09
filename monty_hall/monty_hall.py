from random import randint

def other(door1, door2):
    if door1 == door2:
        return door1 + randint(0,1) + 1 % 3
    else:
        return 3 - (door1 + door2)
    
def step2(player):
    switcher = {
        "Alice": 0,
        "Bob": 0,
        "Dave": randint(0,2),
        "Erin": randint(0,2),
        "Frank": 0,
    }
    return switcher.get(player)

def step4(player, first_choice, open_door):
    switcher = {
        "Alice": first_choice,
        "Bob": other(first_choice, open_door),
        "Dave": first_choice,
        "Erin": other(first_choice, open_door),
        "Frank": 1 if open_door != 1 else first_choice,
    }
    return switcher.get(player)

def monty_hall(name, count):
    wins = 0
    player = name
    gina_win = True
    if player == "Gina":
        player = "Alice"
    for i in range(count):
        if name == "Gina" and gina_win == False:
            player = "Alice" if player == "Bob" else "Bob"
        prize = randint(0,2) # step 1         
        first_choice = step2(player) # step 2
        open_door = other(prize, first_choice) # step 3
        second_choice = step4(player, first_choice, open_door) #step 4
        if second_choice == prize:
            wins += 1
            gina_win = True
        else:
            gina_win = False
    return wins/count*100

def main():
    print("Alice: {r:.2f}%".format(r = monty_hall('Alice', 1000)))
    print("Bob: {r:.2f}%".format(r = monty_hall('Bob', 1000)))
    print("Dave: {r:.2f}%".format(r = monty_hall('Dave', 1000)))
    print("Erin: {r:.2f}%".format(r = monty_hall('Erin', 1000)))
    print("Frank: {r:.2f}%".format(r = monty_hall('Frank', 1000)))
    print("Gina: {r:.2f}%".format(r = monty_hall('Gina', 1000)))
    
if __name__ == "__main__":
    main()