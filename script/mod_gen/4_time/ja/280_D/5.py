def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)
    
k = int(input())
n = 1
while True:
    if factorial(n) % k == 0:
        print(n)
        break
    else:
        n += 1

if __name__ == '__main__':
    factorial()