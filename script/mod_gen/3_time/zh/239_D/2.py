def is_prime(num):
    if num == 1:
        return False
    for i in range(2, int(num**0.5)+1):
        if num % i ==0:
            return False
    return True
a,b,c,d = map(int,input().split())
for i in range(a,b+1):
    if is_prime(i):
        for j in range(c,d+1):
            if is_prime(j):
                if i+j == 2:
                    print("High")
                    exit()
                elif i+j == 3:
                    print("High")
                    exit()
                elif i+j == 5:
                    print("High")
                    exit()
                elif i+j == 7:
                    print("High")
                    exit()
                elif i+j == 11:
                    print("High")
                    exit()
                elif i+j == 13:
                    print("High")
                    exit()
                else:
                    print("Low")
                    exit()

if __name__ == '__main__':
    is_prime()