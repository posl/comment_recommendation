def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    #print(A)
    ans = 0
    for i in range(1, N):
        ans += (A[i] - A[i-1]) * i * (N-i)
    print(ans)
