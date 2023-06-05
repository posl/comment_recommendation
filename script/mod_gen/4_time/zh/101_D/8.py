def S(n):
    s = 0
    while n > 0:
        s += n % 10
        n = n // 10
    return s
k = int(input())
n = 1
while k > 0:
    if S(n) == 1:
        print(n)
        k -= 1
    n += 1

if __name__ == '__main__':
    S()