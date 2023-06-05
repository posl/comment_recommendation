def main():
    n,k = map(int,input().split())
    p = []
    for i in range(n):
        p.append(list(map(int,input().split())))
    for i in range(n):
        if sum(p[i]) + 300 > sum(p[k-1]):
            print('Yes')
        else:
            print('No')
main()
