def main():
    n,k = map(int,input().split())
    s = [input() for _ in range(n)]
    ans = 0
    for i in range(2**n):
        t = []
        for j in range(n):
            if i & 1<<j:
                t.append(s[j])
        if len(t) != k:
            continue
        c = [0] * 26
        for j in t:
            for l in j:
                c[ord(l)-97] += 1
        if max(c) == k:
            ans = max(ans,sum(i>>j&1 for j in range(n)))
    print(ans)

if __name__ == '__main__':
    main()