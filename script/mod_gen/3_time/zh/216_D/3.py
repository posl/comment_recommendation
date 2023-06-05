def main():
    n,m = map(int,input().split())
    k = [0]*m
    a = []
    for i in range(m):
        k[i] = int(input())
        a.append(list(map(int,input().split())))
    print(k)
    print(a)
    print(sum(k))
    if sum(k) == 2*n:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()