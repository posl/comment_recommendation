def main():
    A,B = map(int,input().split())
    if A+B >= 100:
        print(4)
    elif A+B >= 80:
        print(3)
    elif A+B >= 50:
        print(2)
    else:
        print(1)

if __name__ == '__main__':
    main()