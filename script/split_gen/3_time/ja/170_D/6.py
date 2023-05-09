def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    max_a = max(a)
    div = [0] * (max_a + 1)
    for i in range(n):
        div[a[i]] += 1
    ans = 0
    for i in range(1, max_a + 1):
        if div[i] == 0:
            continue
        if div[i] == 1:
            ans += 1
            continue
        if div[i] >= 2:
            ans += 1
            for j in range(i * 2, max_a + 1, i):
                div[j] = 0
    print(ans)
