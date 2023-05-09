def main():
    n, k = map(int, input().split())
    d = [0] * k
    a = [[0] * 100 for _ in range(k)]
    for i in range(k):
        d[i] = int(input())
        a[i][:d[i]] = map(int, input().split())
    ans = 0
    for i in range(1, n+1):
        for j in range(k):
            if i in a[j][:d[j]]:
                break
        else:
            ans += 1
    print(ans)
