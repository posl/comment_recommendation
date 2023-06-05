def main():
    n = int(input())
    a = [int(x) for x in input().split()]
    b = [0] * n
    for i in range(n):
        b[a[i] - 1] = i + 1
    ans = 0
    for i in range(1, n):
        if b[i - 1] > b[i]:
            ans += 1
    print(ans)
