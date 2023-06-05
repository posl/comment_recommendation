def main():
    n,m = map(int,input().split())
    a = []
    b = []
    for i in range(m):
        a1,b1 = map(int,input().split())
        a.append(a1)
        b.append(b1)
    a.sort()
    b.sort()
    if a[0] == 1 and b[-1] == n:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()