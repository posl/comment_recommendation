def main():
    """Main function"""
    animals, legs = map(int, input().split())
    cranes = 0
    turtles = 0
    while cranes <= animals:
        if cranes * 2 + turtles * 4 == legs:
            print("Yes")
            return
        cranes += 1
        turtles = animals - cranes
    print("No")
