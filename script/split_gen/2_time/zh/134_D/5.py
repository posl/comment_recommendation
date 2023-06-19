def main():
    n = int(input())
    a = list(map(int,input().split()))
    b = [0] * n
    c = [0] * n
    for i in range(n):
        if a[i] == 1:
            b[i] = 1
            c[i] = 1
    for i in range(n):
        if b[i] == 1:
            for j in range(i+1,n,i+1):
                b[j] = 1 - b[j]
    for i in range(n-1,-1,-1):
        if c[i] == 1:
            for j in range(i-1,-1,-i):
                c[j] = 1 - c[j]
    d = []
    for i in range(n):
        if b[i] == c[i]:
            d.append(i+1)
    print(len(d))
    if len(d) > 0:
        print(" ".join(map(str,d)))
