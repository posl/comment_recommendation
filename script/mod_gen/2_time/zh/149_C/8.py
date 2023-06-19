def prime_number(n):
    if n < 2:
        return 0
    for i in range(2, int(n**0.5)+1):
        if n%i == 0:
            return 0
    return 1
x = int(input())
while prime_number(x) == 0:
    x += 1
print(x)

if __name__ == '__main__':
    prime_number()