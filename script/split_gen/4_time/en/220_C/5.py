def problem():
    N = int(input())
    A = list(map(int, input().split()))
    X = int(input())
    B = A * 10 ** 100
    sum = 0
    count = 0
    for i in range(len(B)):
        sum += B[i]
        count += 1
        if sum > X:
            print(count)
            break
