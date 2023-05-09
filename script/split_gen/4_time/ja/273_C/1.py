def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = [0] * N
    cnt = [0] * N
    for i in range(N):
        cnt[A[i]-1] += 1
    for i in range(N):
        ans[cnt[i]-1] += 1
    for i in range(N):
        print(ans[i])
