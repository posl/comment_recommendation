def is_prime(n):
    if n == 1:
        return False
    elif n == 2:
        return True
    else:
        for i in range(2,n):
            if n % i == 0:
                return False
        return True
a,b,c,d = map(int,input().split())
for i in range(100):
    if is_prime(a+c+i):
        print("Takahashi")
        exit()
    elif is_prime(b+d+i):
        print("Aoki")
        exit()
