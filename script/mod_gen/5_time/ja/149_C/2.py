def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(n**0.5)+1):
        #print(i)
        if n % i == 0:
            return False
    return True
x = int(input())
while True:
    #print(x)
    if is_prime(x):
        print(x)
        exit()
    x += 1

if __name__ == '__main__':
    is_prime()