def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))
    B_C = [0] * N
    for i in range(N):
        B_C[C[i]-1] += 1
    A_B_C = [0] * N
    for i in range(N):
        A_B_C[B[i]-1] += B_C[i]
    ans = 0
    for i in range(N):
        ans += A_B_C[A[i]-1]
    print(ans)
main()
