def main():
    N = int(input())
    A = list(map(int, input().split()))
    X = int(input())
    # 10^100份的连接
    B = A * 10 ** 100
    # 从左到右相加
    sum = 0
    for i in range(len(B)):
        sum += B[i]
        if sum > X:
            print(i+1)
            break
