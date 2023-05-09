def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    a = [0] + a
    ans = 0
    for i in range(n):
        if a[i] == i + 1:
            ans += 1
            for j in range(i + 1, i + k):
                if j == n: break
                if a[j] == j + 1:
                    ans += 1
                    break
    print(ans)
