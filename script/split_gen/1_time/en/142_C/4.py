def main():
    N = int(input())
    A = list(map(int, input().split()))
    if N == 1:
        print(1)
        return
    ans = [0] * N
    for i in range(N):
        ans[A[i]-1] = i+1
    print(*ans)
