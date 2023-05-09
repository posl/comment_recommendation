def main():
    N = int(input())
    A = list(map(int, input().split()))
    A = [0] + A
    count = 0
    for i in range(N, 0, -1):
        if A[i] <= A[i-1]:
            count += A[i-1] - A[i] + 1
            A[i-1] = A[i] - 1
    print(count)
main()
This is a solution for the following problem.
