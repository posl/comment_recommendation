def is_prime(x):
    if x <= 1:
        return False
    else:
        for i in range(2, x):
            if x % i == 0:
                return False
        else:
            return True
a, b, c, d = map(int, input().split())
for i in range(a, b+1):
    for j in range(c, d+1):
        if is_prime(i+j):
            print("高桥")
            exit()
else:
    print("青木")
