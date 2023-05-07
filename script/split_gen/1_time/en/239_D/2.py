def is_prime(num):
    if num == 1:
        return False
    elif num == 2:
        return True
    else:
        for i in range(2,num):
            if num%i == 0:
                return False
        return True
a,b,c,d = map(int,input().split())
for i in range(a,b+1):
    for j in range(c,d+1):
        if is_prime(i+j):
            print("Aoki")
            exit()
print("Takahashi")
