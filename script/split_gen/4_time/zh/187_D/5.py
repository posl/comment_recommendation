def solve():
    N = int(input())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    # print(A)
    # print(B)
    sum = 0
    for i in range(N):
        sum += A[i]
    # print(sum)
    ave = sum / 2
    # print(ave)
    flag = False
    for i in range(N):
        sum -= A[i]
        if sum < ave:
            flag = True
            print(i + 1)
            break
    if flag == False:
        print(N)
