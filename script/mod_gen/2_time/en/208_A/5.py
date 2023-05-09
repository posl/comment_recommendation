def main():
    A, B = map(int, input().split())
    if A <= B <= A * 6:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()