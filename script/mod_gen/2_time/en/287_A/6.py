def main():
    n = int(input())
    for i in range(n):
        s = input()
        if s == "For":
            print("Yes")
            return
    print("No")
    return

if __name__ == '__main__':
    main()