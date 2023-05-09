def main():
    n = int(input())
    s = input()
    r = 0
    w = 0
    for i in range(n):
        if s[i] == "R":
            r += 1
        else:
            w += 1
    if r == 0 or w == 0:
        print(0)
        exit()
    ans = 0
    for i in range(r):
        if s[i] == "W":
            ans += 1
    print(ans)
main()

if __name__ == '__main__':
    main()