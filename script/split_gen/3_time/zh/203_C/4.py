def main():
    n,k = map(int,input().split())
    ab = [list(map(int,input().split())) for _ in range(n)]
    ab.sort()
    ans = 0
    for a,b in ab:
        if a > k:
            break
        k -= b
        ans = a
    print(ans+k)
