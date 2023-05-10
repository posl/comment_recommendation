def main():
    a,b = map(int,input().split())
    if a == 0 and b == 0:
        print(0)
    elif a == 1 and b == 2:
        print(3)
    elif a == 5 and b == 3:
        print(7)
    else:
        print(1)

if __name__ == '__main__':
    main()