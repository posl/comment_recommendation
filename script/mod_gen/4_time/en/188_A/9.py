def main():
    #input
    X, Y = map(int, input().split())
    #check if the team behind can turn the tables with a successful three-point goal
    if X < Y:
        if X + 3 > Y:
            print("Yes")
        else:
            print("No")
    else:
        print("No")

if __name__ == '__main__':
    main()