def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for x in range(1, max(A)+1):
        cnt = 0
        for i in range(N):
            if A[i] >= x:
                cnt += 1
            else:
                ans = max(ans, cnt*x)
                cnt = 0
        ans = max(ans, cnt*x)
    print(ans)
