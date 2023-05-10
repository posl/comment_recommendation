def check_prime(num):
    for i in range(2,num):
        if num % i == 0:
            return False
    return True

if __name__ == '__main__':
    check_prime()