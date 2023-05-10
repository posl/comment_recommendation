def main():
    n, k = map(int, input().split())
    r, s, p = map(int, input().split())
    t = list(input())
    ans = 0
    for i in range(n):
        if i < k:
            if t[i] == "r":
                ans += p
            elif t[i] == "s":
                ans += r
            else:
                ans += s
        else:
            if t[i] == "r":
                if t[i-k] == "r":
                    t[i] = ""
                else:
                    ans += p
            elif t[i] == "s":
                if t[i-k] == "s":
                    t[i] = ""
                else:
                    ans += r
            else:
                if t[i-k] == "p":
                    t[i] = ""
                else:
                    ans += s
    print(ans)

if __name__ == '__main__':
    main()