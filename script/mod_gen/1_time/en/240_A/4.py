def main():
    a, b = map(int, input().split())
    if a in [1, 3, 5, 7, 8, 10]:
        if b in [4, 6, 9]:
            print("Yes")
        else:
            print("No")
    else:
        print("No")

if __name__ == '__main__':
    main()