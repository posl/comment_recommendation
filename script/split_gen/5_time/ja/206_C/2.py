def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    c = [0] * (n + 1)
    for i in range(n):
        ans += i - c[a[i]]
        c[a[i]] += 1
    print(ans)
