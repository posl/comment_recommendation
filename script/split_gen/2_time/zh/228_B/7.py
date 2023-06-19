def main():
    n,x = map(int,input().split())
    a = list(map(int,input().split()))
    a[x-1] = -1
    b = [0]*n
    for i in range(n):
        if a[i] != -1:
            b[a[i]-1] += 1
    for i in range(n):
        if b[i] != 0:
            b[i] = 1
    print(sum(b))
