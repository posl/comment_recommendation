def main():
    n,x = map(int, input().split())
    a = list(map(int, input().split()))
    a[x-1] = 0
    a = [i-1 for i in a]
    #print(a)
    b = [0 for i in range(n)]
    for i in range(n):
        if a[i] != -1:
            b[a[i]] += 1
    #print(b)
    for i in range(n):
        if b[i] != 0:
            b[i] += 1
    #print(b)
    print(sum(b))

if __name__ == '__main__':
    main()