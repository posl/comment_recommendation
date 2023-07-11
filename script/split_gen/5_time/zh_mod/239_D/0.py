def is_prime(num):
    if num == 1:
        return False
    if num == 2:
        return True
    for i in range(2,int(num**0.5)+1):
