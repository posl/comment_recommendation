def main():
    n,x = map(int, input().split())
    a = []
    b = []
    for i in range(n):
        ai,bi = map(int, input().split())
        a.append(ai)
        b.append(bi)
    sum = 0
    for i in range(n):
        sum += a[i]*b[i]
    if sum <= x:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()