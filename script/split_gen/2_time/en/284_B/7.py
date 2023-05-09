def count_odd():
    T = int(input())
    for i in range(T):
        N = int(input())
        A = input()
        A = A.split()
        A = [int(x) for x in A]
        count = 0
        for j in range(N):
            if A[j] % 2 == 1:
                count += 1
        print(count)
