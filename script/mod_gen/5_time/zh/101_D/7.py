def S(n):
    sum = 0
    while n > 0:
        sum += n % 10
        n //= 10
    return sum
K = int(input())
i = 1
while K > 0:
    if S(i) == 1:
        print(i)
        K -= 1
    i += 1

if __name__ == '__main__':
    S()