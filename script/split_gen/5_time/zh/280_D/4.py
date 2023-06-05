def get_prime_num(n):
    prime_num = []
    for i in range(2, n + 1):
        if i > 10 and i % 10 in [1, 3, 7, 9]:
            for j in prime_num:
                if i % j == 0:
                    break
            else:
                prime_num.append(i)
        elif i <= 10:
            prime_num.append(i)
    return prime_num
