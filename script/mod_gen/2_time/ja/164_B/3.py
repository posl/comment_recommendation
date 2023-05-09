def main():
    A, B, C, D = map(int, input().split())
    if (C + D - 1) // D <= (A + B - 1) // B:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()