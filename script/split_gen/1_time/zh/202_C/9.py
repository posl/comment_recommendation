def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))
    from collections import Counter
    c = Counter(c)
    ans = 0
    for i in range(1, n+1):
        ans += c[b[a[i-1]-1]]
    print(ans)
