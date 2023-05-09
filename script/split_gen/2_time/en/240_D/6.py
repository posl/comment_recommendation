def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = [0 for _ in range(2 * 10 ** 5 + 1)]
    ans = 0
    for i in range(n):
        b[a[i]] += 1
        if b[a[i]] == 1:
            ans += 1
        else:
            ans -= 1
    print(ans)
