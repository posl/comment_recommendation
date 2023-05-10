def main():
    n = input()
    k = len(n)
    ans = 10**9
    for i in range(2**k):
        s = ""
        for j in range(k):
            if (i >> j) & 1:
                s += n[j]
        if s == "":
            continue
        if int(s) % 3 == 0:
            ans = min(ans,k-len(s))
    if ans == 10**9:
        print(-1)
    else:
        print(ans)

if __name__ == '__main__':
    main()