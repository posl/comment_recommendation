def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort(reverse=True)
    res = -1
    for i in range(n-1):
        for j in range(i+1, n):
            if (a[i] + a[j]) % 2 == 0:
                res = max(res, a[i] + a[j])
                break
    print(res)
