def main():
    #Read input
    X, Y = map(int, input().split())
    
    #Solve problem
    if X < Y:
        if Y - X < 3:
            print("Yes")
        else:
            print("No")
    else:
        if X - Y < 3:
            print("Yes")
        else:
            print("No")

if __name__ == '__main__':
    main()