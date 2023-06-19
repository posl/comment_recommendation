def main():
    N = int(input())
    # 1. N是素数，直接输出0
    if is_prime(N):
        print(0)
        return
    # 2. N不是素数，分解质因数
    else:
        factor = prime_factorization(N)
        # print(factor)
        # 3. 分解质因数中，出现1次的质因数个数
        count = 0
        for key, value in factor.items():
            if value == 1:
                count += 1
        print(count)
