def problem101_b():
    n = int(input())
    sum = 0
    for i in str(n):
        sum += int(i)
    if n % sum == 0:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    problem101_b()