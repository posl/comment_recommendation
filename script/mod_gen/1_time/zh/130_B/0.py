def main():
    n,x = map(int,input().split())
    l = list(map(int,input().split()))
    d = [0]
    for i in range(n):
        d.append(d[i]+l[i])
    for i in range(n+1):
        if d[i]>x:
            print(i)
            break

if __name__ == '__main__':
    main()