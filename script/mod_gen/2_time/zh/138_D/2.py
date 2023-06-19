def main():
    n,q = map(int,input().split())
    a = [0 for _ in range(n)]
    for _ in range(n-1):
        i,j = map(int,input().split())
        a[i-1] += 1
        a[j-1] += 1
    for _ in range(q):
        p,x = map(int,input().split())
        a[p-1] += x
    print(*a)

if __name__ == '__main__':
    main()