def prime(n):
    if n%2 == 0:
        return False
    for i in range(3,int(n**0.5)+1,2):
        if n%i == 0:
            return False
    return True
t = int(input())
for i in range(t):
    n = int(input())
    p = int(n**0.5)
    while True:
        if prime(p) and n%p == 0:
            q = n//p//p
            if prime(q):
                print(p,q)
                break
        p += 1

if __name__ == '__main__':
    prime()