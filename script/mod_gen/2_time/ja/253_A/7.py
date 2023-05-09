def main():
    a, b, c = map(int, input().split())
    if a > b:
        if b > c:
            print("Yes")
        elif a > c:
            print("Yes")
        else:
            print("No")
    elif a < b:
        if a > c:
            print("No")
        elif b > c:
            print("No")
        else:
            print("Yes")
    else:
        print("Yes")

if __name__ == '__main__':
    main()