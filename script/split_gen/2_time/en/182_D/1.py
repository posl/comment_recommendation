def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    tmp = 0
    for i in range(N):
        tmp += A[i]
        ans = max(ans, tmp)
        if ans < 0:
            ans = 0
        if tmp < 0:
            tmp = 0
    print(ans)
