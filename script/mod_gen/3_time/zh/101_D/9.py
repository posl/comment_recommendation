def snuke(n):
    sum = 0
    while n > 0:
        sum += n % 10
        n //= 10
    return sum
k = int(input())
n = 1
while k > 0:
    if snuke(n) == 1:
        print(n)
        k -= 1
    n += 1

if __name__ == '__main__':
    snuke()