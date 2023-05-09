def get_prime_list(N):
    prime_list = [2]
    for i in range(3, N+1, 2):
        for j in range(3, i, 2):
            if i % j == 0:
                break
        else:
            prime_list.append(i)
    return prime_list

if __name__ == '__main__':
    get_prime_list()