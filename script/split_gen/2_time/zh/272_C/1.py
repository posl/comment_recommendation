def main():
    n, m = map(int, input().split())
    a = [0] * m
    for i in range(m):
        a[i] = list(map(int, input().split()))
    ans = 0
    for i in range(1, n + 1):
        for j in range(i + 1, n + 1):
            for k in range(m):
                if i in a[k] and j in a[k]:
                    ans += 1
                    break
    if ans == n * (n - 1) // 2:
        print("Yes")
    else:
        print("No")
