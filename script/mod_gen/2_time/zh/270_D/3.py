def main():
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    a.append(n)
    a.insert(0,0)
    a.sort()
    s = 0
    for i in range(k+1):
        s += a[i]
    print(s)

if __name__ == '__main__':
    main()