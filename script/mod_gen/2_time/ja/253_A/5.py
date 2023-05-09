def main():
    a, b, c = map(int, input().split())
    if b < a < c or c < a < b:
        print("Yes")
    elif a < b < c or c < b < a:
        print("Yes")
    elif a < c < b or b < c < a:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()