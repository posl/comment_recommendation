def main():
    n = int(input())
    s = input()
    c = 0
    for i in range(n-2):
        if s[i:i+3] == "ABC":
            c += 1
    print(c)

if __name__ == '__main__':
    main()