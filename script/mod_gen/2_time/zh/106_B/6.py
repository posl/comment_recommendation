def get_divisor_count(n):
    count = 0
    for i in range(1, int(n**0.5+1)):
        if n % i == 0:
            count += 2
    if int(n**0.5)**2 == n:
        count -= 1
    return count

if __name__ == '__main__':
    get_divisor_count()