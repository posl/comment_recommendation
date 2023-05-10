def main():
    a, b = map(int, input().split())
    if a == 8 and b == 13 or a == 13 and b == 8:
        print("Yes")
    elif a == 5 and b == 12 or a == 12 and b == 5:
        print("Yes")
    elif a == 1 and b == 14 or a == 14 and b == 1:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()