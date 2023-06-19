def problem101_b(n):
    sum = 0
    for i in range(len(n)):
        sum += int(n[i])
    if int(n) % sum == 0:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    problem101_b()