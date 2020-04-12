import random
n = random.randint(1, 99)
manasu = int(raw_input("Enter an integer from 1 to 99: "))
while n != "manasu":
    print
    if manasu < n:
        print "guess is low"
        manasu = int(raw_input("Enter an integer from 1 to 99: "))
    elif manasu > n:
        print "guess is high"
        manasu = int(raw_input("Enter an integer from 1 to 99: "))
    else:
        print "you guessed it!"
        break
    print
