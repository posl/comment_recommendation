def main():
    # Take input Here and Call solution function
    r,c = map(int,input().strip().split())
    if r%2 == 0 and c%2 == 0:
        print("white")
    elif r%2 == 0 and c%2 != 0:
        print("black")
    elif r%2 != 0 and c%2 == 0:
        print("black")
    elif r%2 != 0 and c%2 != 0:
        print("white")
    return 0
