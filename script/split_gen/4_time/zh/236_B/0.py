def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(1, N+1):
        ans ^= i
    for i in range(4*N-1):
        ans ^= A[i]
    print(ans)
