def main():
    n = int(input())
    t = [int(x) for x in input().split()]
    t.sort()
    ans = t[0]
    for i in range(1,n):
        ans += t[i]
    ans -= t[0]//2
    print(ans)
