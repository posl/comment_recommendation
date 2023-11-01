def get_prime_list(number):
    prime_list = []
    for i in range(2, number + 1):
        flag = True
        for j in range(2, i):
            if i % j == 0:
