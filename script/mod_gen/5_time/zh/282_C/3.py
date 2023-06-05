def main():
    n = int(input())
    s = input()
    for i in range(0, n):
        if i % 2 == 0:
            if s[i] == "\"":
                print(s[i], end="")
            else:
                print(".", end="")
        else:
            print(s[i], end="")

if __name__ == '__main__':
    main()