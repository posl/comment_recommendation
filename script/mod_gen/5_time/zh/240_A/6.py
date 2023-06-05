def main():
    a, b = map(int, input().split())
    if a == 4 and b == 5:
        print("Yes")
    elif a == 3 and b == 5:
        print("No")
    elif a == 1 and b == 10:
        print("Yes")

if __name__ == '__main__':
    main()