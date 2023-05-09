def calc(n):
    sum = 0
    for i in range(1, n + 1):
        sum += i
        if sum >= n:
            return i
n = int(input())
print(calc(n))

if __name__ == '__main__':
    calc()