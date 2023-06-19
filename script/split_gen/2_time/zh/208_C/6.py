def main():
    N,K = map(int,input().split())
    a = list(map(int,input().split()))
    a.sort()
    print(a)
    b = [0]*N
    for i in range(N):
        if i == 0:
            b[i] = a[i]
        else:
            b[i] = a[i] - a[i-1]
    print(b)
    for i in range(N):
        if i == 0:
            b[i] = b[i]
        else:
            b[i] = b[i-1] + b[i]
    print(b)
    for i in range(N):
        if i == 0:
            b[i] = b[i]
        else:
            b[i] = b[i-1] + b[i]
    print(b)
    for i in range(N):
        if i == 0:
            b[i] = b[i]
        else:
            b[i] = b[i-1] + b[i]
    print(b)
    for i in range(N):
        if i == 0:
            b[i] = b[i]
        else:
            b[i] = b[i-1] + b[i]
    print(b)
    for i in range(N):
        if i == 0:
            b[i] = b[i]
        else:
            b[i] = b[i-1] + b[i]
    print(b)
    for i in range(N):
        if i == 0:
            b[i] = b[i]
        else:
            b[i] = b[i-1] + b[i]
    print(b)
    for i in range(N):
        if i == 0:
            b[i] = b[i]
        else:
            b[i] = b[i-1] + b[i]
    print(b)
    for i in range(N):
        if i == 0:
            b[i] = b[i]
        else:
            b[i] = b[i-1] + b[i]
    print(b)
    for i in range(N):
        if K >= b[i]:
            print(a[i])
        else:
            print(a[i] - (b[i] - K))
            break
