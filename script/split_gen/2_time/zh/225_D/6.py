def main():
    n,m = map(int,input().split())
    b = []
    for i in range(n):
        b.append(list(map(int,input().split())))
    a = []
    for i in range(1,10**100+1):
        temp = []
        for j in range(1,8):
            temp.append((i-1)*7+j)
        a.append(temp)
    for i in range(0,10**100-n+1):
        for j in range(0,7-m+1):
            if a[i][j:j+m] == b[0]:
                for k in range(1,n):
                    if a[i+k][j:j+m] != b[k]:
                        break
                    if k == n-1:
                        print('Yes')
                        return
    print('No')
    return
