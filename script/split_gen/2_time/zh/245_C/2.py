def problems245_b():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    num = 0
    for i in range(N):
        if A[i] > num:
            print(num)
            return
        elif A[i] == num:
            num += 1
    print(num)
    return
