def main():
    N = int(input())
    A = list(map(int, input().split()))
    
    count = [0] * (N+1)
    for a in A:
        count[a] += 1
    ans = [0] * N
    for i in range(N):
        ans[i] = count[A[i]] - 1
    for a in A:
        print(ans[a])
