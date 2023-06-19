def main():
    n,k = map(int, input().split())
    s = []
    for i in range(n):
        s.append(input())
    ans = 0
    for i in range(1<<n):
        t = set()
        for j in range(n):
            if i&(1<<j):
                t |= set(s[j])
        if len(t) == k:
            ans = max(ans, bin(i).count("1"))
    print(ans)
