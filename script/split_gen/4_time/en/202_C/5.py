def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))
    B_C = [0]*N
    for i in range(N):
        B_C[C[i]-1] += 1
    ans = 0
    for i in range(N):
        ans += B_C[B[A[i]-1]-1]
    print(ans)
