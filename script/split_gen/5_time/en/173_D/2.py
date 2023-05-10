def problems173_d():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort(reverse=True)
    result = 0
    for i in range(1, N):
        result += A[i // 2]
    print(result)
