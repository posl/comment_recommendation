def solve():
    N = int(input())
    A = list(map(int, input().split()))
    X = int(input())
    B = A * 10 ** 100
    sum = 0
    for i in range(len(B)):
        sum += B[i]
        if sum > X:
            print(i + 1)
            break
