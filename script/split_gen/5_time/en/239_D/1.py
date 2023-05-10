def prime(num):
    if num < 2:
        return False
    elif num == 2:
        return True
    for i in range(2,num):
        if num % i == 0:
            return False
    return True
A,B,C,D = map(int,input().split())
for i in range(A,B+1):
    for j in range(C,D+1):
        if prime(i+j):
            print("Takahashi")
            exit()
        else:
            continue
print("Aoki")
