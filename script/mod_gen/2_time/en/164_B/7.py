def main():
    A, B, C, D = map(int, input().split())
    if A <= D * C:
        print("No")
    else:
        print("Yes")

if __name__ == '__main__':
    main()