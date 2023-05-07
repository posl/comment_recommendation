def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    a = [i - 1 for i in a]
    ans = 0
    while True:
        if a == list(range(n)):
            break
        for i in range(n - k + 1):
            if a[i] == a[i + k - 1]:
                continue
            min_a = min(a[i:i + k])
            for j in range(i, i + k):
                a[j] = min_a
        ans += 1
    print(ans)
