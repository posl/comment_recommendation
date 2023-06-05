def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    s = [0] * (n + 1)
    for i in range(n):
        s[i + 1] = s[i] + 1
        for j in range(k):
            if i + 1 - a[j] >= 0:
                s[i + 1] = min(s[i + 1], s[i + 1 - a[j]])
            else:
                break
        s[i + 1] = 1 - s[i + 1]
    print(s[n])
