def get_prime(n):
    prime_list = [2]
    for i in range(3, n+1):
        for j in prime_list:
            if i % j == 0:
                break
            if j >= i ** 0.5:
                prime_list.append(i)
                break
    return prime_list

if __name__ == '__main__':
    get_prime()