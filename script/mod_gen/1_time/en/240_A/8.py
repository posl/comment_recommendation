def main():
    a, b = map(int, input().split())
    if (b-a) == 1 or (a+b)%2 == 0:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()