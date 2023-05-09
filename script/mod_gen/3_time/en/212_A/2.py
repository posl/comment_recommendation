def main():
    a, b = map(int, input().split())
    if a == 0 and b != 0:
        print("Silver")
    elif a != 0 and b == 0:
        print("Gold")
    else:
        print("Alloy")

if __name__ == '__main__':
    main()