def main():
    n,m = map(int,input().split())
    a_b = []
    for i in range(m):
        a_b.append(list(map(int,input().split())))
    k = int(input())
    c_d = []
    for i in range(k):
        c_d.append(list(map(int,input().split())))
    #print(n,m,a_b,k,c_d)
    ans = 0
    for i in range(2**k):
        flag = [0]*n
        for j in range(k):
            if i>>j & 1:
                flag[c_d[j][0]-1] = 1
            else:
                flag[c_d[j][1]-1] = 1
        tmp = 0
        for j in range(m):
            if flag[a_b[j][0]-1] and flag[a_b[j][1]-1]:
                tmp += 1
        ans = max(ans,tmp)
    print(ans)
main()
