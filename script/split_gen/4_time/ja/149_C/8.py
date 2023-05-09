def is_prime(num):
    if num == 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
 
    for i in range(3, int(num**0.5)+1, 2):
        if num % i == 0:
            return False
 
    return True
x = int(input())
while True:
    if is_prime(x):
        print(x)
        break
    else:
        x += 1
