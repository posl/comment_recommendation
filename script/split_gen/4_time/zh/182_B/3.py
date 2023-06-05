def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for k in range(2, 1001):
        cnt = 0
        for i in range(n):
            if a[i] % k == 0:
                cnt += 1
        if cnt > ans:
            ans = cnt
            ans_k = k
    print(ans_k)
