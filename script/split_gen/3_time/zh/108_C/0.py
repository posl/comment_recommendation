def main():
    N, K = map(int, input().split())
    if K % 2 == 0:
        # K为偶数
        a = N // K
        b = N // (K // 2) - a
        c = N // (K // 2) - a
    else:
        # K为奇数
        a = N // K
        b = N // ((K + 1) // 2) - a
        c = N // ((K + 1) // 2) - a
    print(a ** 3 + b ** 3 + c ** 3)
