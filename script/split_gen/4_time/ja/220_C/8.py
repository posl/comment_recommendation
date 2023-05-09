def main():
    # input
    N = int(input())
    A = list(map(int, input().split()))
    X = int(input())
    # compute
    # 1. 1回分の和を求める
    sum_A = sum(A)
    # 2. 1回分の和で割って何回繰り返せるか求める
    count = X // sum_A
    # 3. 何回繰り返せるか求める
    result = count * N
    # 4. 余りを求める
    X = X % sum_A
    # 5. 残りの和を求める
    sum_A = 0
    for i in range(N):
        sum_A += A[i]
        if sum_A > X:
            result += i + 1
            break
    # output
    print(result)
    return
