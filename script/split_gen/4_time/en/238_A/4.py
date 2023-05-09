def main():
    n = int(input())
    # 2^n > n^2
    # 2^n > n * n
    # 2^n > n * n
    # 2^n - n * n > 0
    # 2^n - n^2 > 0
    if 2**n > n**2:
        print('Yes')
    else:
        print('No')
