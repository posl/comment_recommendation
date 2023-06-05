def main():
    n,k,q = map(int,input().split())
    a = list(map(int,input().split()))
    l = list(map(int,input().split()))
    #棋子的位置
    pos = [0] * n
    for i in range(k):
        pos[a[i]-1] += 1
    for i in range(n-1,0,-1):
        pos[i-1] += pos[i]
    for i in range(q):
        print(pos[l[i]-1])

if __name__ == '__main__':
    main()