def main():
    X,Y = map(int,input().split())
    if X < Y:
        if X+3 > Y:
            print("Yes")
        else:
            print("No")
    else:
        if Y+3 > X:
            print("Yes")
        else:
            print("No")

if __name__ == '__main__':
    main()