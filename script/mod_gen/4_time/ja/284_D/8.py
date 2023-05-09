def get_prime_numbers(n):
    prime_numbers = []
    # 2からnまでの整数を素数判定する
    for i in range(2, n + 1):
        # 2からi-1までの整数で割り切れるかどうかを判定
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            prime_numbers.append(i)
    return prime_numbers

if __name__ == '__main__':
    get_prime_numbers()