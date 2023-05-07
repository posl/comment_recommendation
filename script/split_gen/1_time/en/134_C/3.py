def main():
    N = int(input())
    A = [int(input()) for _ in range(N)]
    A.sort()
    max_A = A[-1]
    for i in range(N):
        if A[i] == max_A:
            print(A[-2])
        else:
            print(max_A)
main()
