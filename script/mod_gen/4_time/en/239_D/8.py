def is_prime(n):
    if n == 1:
        return False
    elif n == 2:
        return True
    else:
        for i in range(2, int(n**0.5)+1):
            if n%i == 0:
                return False
    return True
a, b, c, d = map(int, input().split())
takahashi = False
for i in range(a, b+1):
    for j in range(c, d+1):
        if is_prime(i+j):
            takahashi = True
            break

if __name__ == '__main__':
    is_prime()