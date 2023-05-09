def S(n):
    sum = 0
    while n > 0:
        sum += n % 10
        n = n // 10
    return sum
k = int(input())
n = 1
while k > 0:
    if n / S(n) <= (n + 1) / S(n + 1):
        print(n)
        k -= 1
    n += 1

if __name__ == '__main__':
    S()