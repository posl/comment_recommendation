def problem213_b():
    N = int(input())
    A = list(map(int, input().split()))
    #print(N)
    #print(A)
    sorted_A = sorted(A)
    #print(sorted_A)
    print(A.index(sorted_A[1]) + 1)
