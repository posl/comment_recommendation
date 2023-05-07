def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    for i in range(N):
        if abs(A[i] - B[i]) > K:
            print("No")
            return
    print("Yes")
main()
The first line is the input of N and K. The second line is the input of A. The third line is the input of B. The fourth line is the output of Yes or No.
