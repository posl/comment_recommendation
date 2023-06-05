def main():
    n = int(input())
    a = list(map(int,input().split()))
    #print(n,a)
    b = [0]*n
    for i in range(n-1):
        b[i] = a[i]
        if b[i] == 2:
            b[i] = 0
        elif b[i] % 2 == 0:
            b[i] -= 1
    #print(b)
    for i in range(n-1):
        if b[i] == 0:
            b[i+1] = 0
    #print(b)
    for i in range(n):
        print(n-sum(b[:i+1]))
