def check(num):
    for i in range(1,10):
        if num % i == 0 and num // i < 10:
            return True
    return False
n = int(input())
