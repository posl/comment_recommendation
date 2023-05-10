def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    for i in range(40, -1, -1):
        if k & (1 << i):
            tmp = 0
            for j in range(n):
                if a[j] & (1 << i):
                    tmp += 1 << i
                else:
                    if tmp + (1 << i) <= k:
                        tmp += 1 << i
            k = tmp
    ans = 0
    for i in range(n):
        ans += k ^ a[i]
    print(ans)
