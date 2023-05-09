def main():
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    a = [x-1 for x in a]
    #print(a)
    #print(n)
    #print(x)
    #print(a)
    b = [0]*n
    b[x-1] = 1
    #print(b)
    for i in range(n):
        if b[i] == 1:
            b[a[i]] = 1
    #print(b)
    print(sum(b))
