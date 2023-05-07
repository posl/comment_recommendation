def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = []
    for i in range(N):
        B.append(A[i])
        if i >= M:
            B[i] += B[i - M]
    B.sort(reverse=True)
    print(sum(B[:M]))
main()
The following code is the solution to the following problem.
