def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    b = [0] * n
    b[0] = a[0]
    for i in range(1, n):
        b[i] = b[i - 1] + a[i]
    ans = 0
    for i in range(n):
        if b[i] * 2 >= a[i]:
            ans += 1
        else:
            ans = 0
    print(ans)
