def main():
    n, k = map(int, input().split())
    c = list(map(int, input().split()))
    cnt = [0] * 10**9
    for i in range(k):
        cnt[c[i]-1] += 1
    ans = 0
    for i in range(10**9):
        if cnt[i] > 0:
            ans += 1
    for i in range(n-k):
        cnt[c[i]-1] -= 1
        cnt[c[i+k]-1] += 1
        tmp = 0
        for j in range(10**9):
            if cnt[j] > 0:
                tmp += 1
        if tmp > ans:
            ans = tmp
    print(ans)
