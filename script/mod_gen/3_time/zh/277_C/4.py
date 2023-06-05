def main():
    n = int(input())
    a, b = [], []
    for i in range(n):
        ai, bi = map(int, input().split())
        a.append(ai)
        b.append(bi)
    a.sort()
    b.sort()
    if n%2 == 0:
        x = n//2
        y = x-1
        print(b[y]-a[x]+1)
    else:
        x = n//2
        print(b[x]-a[x]+1)

if __name__ == '__main__':
    main()