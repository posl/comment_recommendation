def main():
    A,B = map(int,input().split())
    if A <= 100 and A >= 1 and B <= 1000 and B >= 1:
        if B % 2 == 0:
            if A <= B / 2:
                print("Yes")
            else:
                print("No")
        else:
            if A <= B / 2 + 1:
                print("Yes")
            else:
                print("No")
    else:
        print("No")

if __name__ == '__main__':
    main()