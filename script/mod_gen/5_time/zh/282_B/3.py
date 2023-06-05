def main():
    n,m = map(int,input().split())
    l = []
    for i in range(n):
        l.append(input())
    cnt = 0
    for i in range(n):
        for j in range(i+1,n):
            for k in range(m):
                if l[i][k] == 'o' or l[j][k] == 'o':
                    if k == m-1:
                        cnt += 1
                else:
                    break
    print(cnt)

if __name__ == '__main__':
    main()