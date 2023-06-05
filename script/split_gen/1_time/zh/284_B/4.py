def problems284_b():
    T = int(input())
    for i in range(T):
        N = int(input())
        A = [int(_) for _ in input().split()]
        count = 0
        for j in range(N):
            if A[j] % 2 == 1:
                count += 1
        print(count)
