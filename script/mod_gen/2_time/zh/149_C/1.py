def is_prime(x):
    if x == 1:
        return False
    elif x == 2:
        return True
    else:
        for i in range(2,x):
            if x % i == 0:
                return False
        return True

if __name__ == '__main__':
    is_prime()