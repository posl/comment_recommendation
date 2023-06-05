def main():
    a,b = map(int,input().split())
    if a == 0 and b == 0:
        print(0)
    elif a == 0 and b != 0:
        print(b)
    elif a != 0 and b == 0:
        print(a)
    else:
        print(7-a-b)

if __name__ == '__main__':
    main()