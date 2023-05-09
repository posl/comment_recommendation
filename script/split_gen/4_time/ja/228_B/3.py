def main():
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    a = [i - 1 for i in a]
    b = [0] * n
    b[x - 1] = 1
    ans = 1
    for i in range(n):
        if b[a[i]] == 1:
            ans += 1
            b[i] = 1
    print(ans)
