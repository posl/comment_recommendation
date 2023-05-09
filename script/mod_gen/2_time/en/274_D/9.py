def main():
    n,x,y = map(int, input().split())
    a = list(map(int, input().split()))
    a.append(0)
    a = [0] + a
    #print(a)
    for i in range(1, n+1):
        for j in range(i+1, n+2):
            if i == j:
                continue
            d = abs(i-j)
            if i < j:
                d = min(d, abs(x-i)+1+abs(y-j))
            else:
                d = min(d, abs(y-i)+1+abs(x-j))
            if a[d] == 0:
                a[d] = 1
    for i in range(1, n+1):
        if a[i] == 0:
            print('No')
            return
    print('Yes')

if __name__ == '__main__':
    main()