def check_legs(x,y):
    '''
    x = cranes
    y = turtles
    '''
    if x*2 + y*4 == legs:
        return True
    else:
        return False
legs = input("How many legs does the animals have in total? ")
legs = int(legs)
cranes = input("How many cranes are there? ")
cranes = int(cranes)
turtles = input("How many turtles are there? ")
turtles = int(turtles)

if __name__ == '__main__':
    check_legs()