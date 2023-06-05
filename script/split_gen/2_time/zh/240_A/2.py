def is_prime(x):
    if x == 1:
        return False
    for i in range(2,int(x**0.5)+1):
        if x % i == 0:
            return False
    return True
A,B,C,D = map(int,input().split())
for i in range(B+1,D+2):
    if is_prime(i):
        if i == A+C or i == A+D or i == B+C or i == B+D:
            print("High")
            exit()
print("Low")
