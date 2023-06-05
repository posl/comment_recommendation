def main():
    n = int(input())
    a = list(map(int,input().split()))
    b = [0] * n
    for i in range(n):
        b[a[i]-1] = i+1
    c = 0
    for i in range(n):
        if b[i] != i+1:
            c += 1
    if c == 0:
        print(0)
    elif c == 2:
        print(1)
    else:
        print(-1)
