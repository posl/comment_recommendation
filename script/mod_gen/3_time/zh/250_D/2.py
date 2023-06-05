def get_prime(n):
    prime_list = [2]
    for i in range(3, n+1, 2):
        flag = True
        for j in prime_list:
            if i % j == 0:
                flag = False
                break
        if flag:
            prime_list.append(i)
    return prime_list

if __name__ == '__main__':
    get_prime()