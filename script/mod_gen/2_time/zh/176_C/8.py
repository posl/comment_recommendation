def main():
    N = int(input())
    A = list(map(int, input().split()))
    if N == 1:
        print(A[0])
        exit()
    if N == 2:
        print(max(A[0], A[1]))
        exit()
    max_h = 0
    for i in range(N):
        max_h = max(max_h, A[i])
        if i > 0:
            if A[i] > A[i - 1]:
                A[i] = A[i - 1]
    print(max_h)
main()
