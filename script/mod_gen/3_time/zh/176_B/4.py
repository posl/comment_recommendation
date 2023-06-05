def is_divisible_by_9(n):
    sum = 0
    for i in range(len(n)):
        sum += int(n[i])
    if sum % 9 == 0:
        return True
    else:
        return False

if __name__ == '__main__':
    is_divisible_by_9()