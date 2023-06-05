def main():
    n = int(input())
    a = list(map(int, input().split()))
    #print(n, a)
    b = [0] * (n+1)
    for i in range(n):
        if a[i] > n:
            continue
        b[a[i]] += 1
    ans = 0
    for i in range(1, n+1):
        if b[i] == 0:
            continue
        ans += b[i] * (b[i]-1) // 2
    print(ans)
