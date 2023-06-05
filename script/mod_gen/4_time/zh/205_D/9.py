def main():
    n,q = map(int,input().split())
    a = list(map(int,input().split()))
    k = []
    for i in range(q):
        k.append(int(input()))
    a.sort()
    a.insert(0,0)
    a.append(a[-1]+1)
    for i in range(q):
        for j in range(1,n+2):
            if a[j-1] < k[i] and k[i] <= a[j]:
                print(k[i]+j-1)
                break

if __name__ == '__main__':
    main()