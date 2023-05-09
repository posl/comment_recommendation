def dice(n):
    sum = 0
    for i in range(1,7):
        sum += i
        if sum == n:
            return True
    return False
a, b = map(int, input().split())

if __name__ == '__main__':
    dice()