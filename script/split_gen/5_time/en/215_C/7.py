def main():
    s, k = input().split()
    k = int(k)
    s = list(s)
    s.sort()
    ans = ''
    while (len(s) > 0):
        n = len(s)
        fact = 1
        for i in range(1, n):
            fact *= i
        q = k // fact
        r = k % fact
        ans += s[q]
        del s[q]
        k = r
    print(ans)
main()
