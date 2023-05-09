def main():
    n,k = map(int,input().split())
    s = [input() for _ in range(n)]
    ans = 0
    for i in range(1<<n):
        if bin(i).count("1") != k:
            continue
        c = set()
        for j in range(n):
            if i>>j & 1:
                for k in s[j]:
                    c.add(k)
        ans = max(ans,len(c))
    print(ans)
