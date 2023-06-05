def main():
    n,m = map(int,input().split())
    a = []
    b = []
    for i in range(m):
        a.append(list(map(int,input().split())))
    for i in range(m):
        b.append(list(map(int,input().split())))
    a.sort()
    b.sort()
    if a == b:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()