def main():
    n,k = map(int,input().split())
    p = []
    for i in range(n):
        p.append(list(map(int,input().split())))
    for i in range(n):
        p[i].sort()
    for i in range(n):
        if p[i][0] + p[i][1] + p[i][2] + 1 >= k:
            print('Yes')
        else:
            print('No')

if __name__ == '__main__':
    main()