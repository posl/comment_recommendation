def main():
    n,m = map(int,input().split())
    a = []
    b = []
    for i in range(m):
        a_i,b_i = map(int,input().split())
        a.append(a_i)
        b.append(b_i)
    a.sort()
    b.sort()
    if a[m-1] < b[0]:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()