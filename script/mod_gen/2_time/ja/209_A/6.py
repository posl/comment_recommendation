def main():
    A,B = map(int, input().split())
    if A > B:
        print(0)
    elif A <= B:
        print(B-A+1)

if __name__ == '__main__':
    main()