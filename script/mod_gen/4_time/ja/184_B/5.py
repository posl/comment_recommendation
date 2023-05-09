def main():
    n, x = map(int, input().split())
    s = input()
    p = x
    for i in range(n):
        if s[i] == "o":
            p += 1
        else:
            if p > 0:
                p -= 1
    print(p)

if __name__ == '__main__':
    main()