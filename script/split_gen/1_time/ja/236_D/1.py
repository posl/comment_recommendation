def main():
    N = int(input())
    A = [list(map(int, input().split())) for _ in range(2*N-1)]
    ans = 0
    for i in range(2*N-1):
        for j in range(i+1, 2*N-1):
            ans ^= A[i][j-i-1]
    print(ans)
