def is_prime(num):
    if num == 1:
        return False
    for i in range(2,num):
        if num % i == 0:
            return False

if __name__ == '__main__':
    is_prime()