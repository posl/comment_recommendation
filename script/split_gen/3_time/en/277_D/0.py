def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    b = [0] * m
    for i in range(n):
        b[a[i]] += 1
    ans = 0
    for i in range(m):
        if b[i] > 1:
            b[i+1] += b[i] - 1
        elif b[i] == 0:
            ans += i
            break
    for i in range(m-1, -1, -1):
        if b[i] == 0:
            ans += m - 1 - i
            break
    print(ans)
