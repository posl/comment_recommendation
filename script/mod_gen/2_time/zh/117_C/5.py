def main():
    n,m = map(int,input().split())
    x = list(map(int,input().split()))
    x.sort()
    #print(x)
    if n == 1:
        print(abs(x[0]-x[m-1]))
        return
    l = []
    for i in range(m-1):
        l.append(x[i+1]-x[i])
    l.sort()
    print(sum(l[:m-n]))

if __name__ == '__main__':
    main()