def main():
    n,k = map(int,input().split())
    p = []
    for i in range(n):
        p.append(list(map(int,input().split())))
    for i in range(n):
        p[i].sort(reverse=True)
        if sum(p[i][:3]) >= k:
            print('Yes')
        else:
            print('No')

if __name__ == '__main__':
    main()