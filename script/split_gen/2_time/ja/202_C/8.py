def main():
    N = int(input())
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    C = list(map(int,input().split()))
    cnt = [0 for _ in range(N+1)]
    for i in range(N):
        cnt[B[C[i]-1]] += 1
    ans = 0
    for i in range(N):
        ans += cnt[A[i]]
    print(ans)
