def main():
    n = int(input())
    a = list(map(int,input().split()))
    s = set(a)
    d = {}
    for i in s:
        d[i] = a.count(i)
    ans = 0
    for i in d.values():
        ans += i*(n-i)
    print(ans//2)
