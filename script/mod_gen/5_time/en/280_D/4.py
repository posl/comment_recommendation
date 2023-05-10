def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
K = int(input())
N = 2
while True:
    if factorial(N) % K == 0:
        print(N)
        break
    N += 1

if __name__ == '__main__':
    factorial()