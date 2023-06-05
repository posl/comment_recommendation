def main():
    A,B = map(int,input().split())
    if B % A == 0 and A <= B/6:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()