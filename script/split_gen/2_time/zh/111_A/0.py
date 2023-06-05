def get_prime_list(num):
    prime_list = []
    for i in range(2, num+1):
        if num % i == 0:
            prime_list.append(i)
            num = num // i
            if num == 1:
                break
    return prime_list
