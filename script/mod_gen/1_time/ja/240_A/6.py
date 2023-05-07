def main():
    a, b = map(int, input().split())
    if a == 1 and b == 10:
        print("Yes")
    elif a == 1 or b == 1 or a == 10 or b == 10:
        print("No")
    else:
        print("Yes")

if __name__ == '__main__':
    main()