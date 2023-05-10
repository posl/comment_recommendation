def main():
    n,m = map(int,input().split())
    cake = []
    for i in range(n):
        x,y,z = map(int,input().split())
        cake.append([x,y,z])
    #print(cake)
    ans = 0
    for i in range(2**3):
        flag = [0]*3
        for j in range(3):
            if (i>>j)&1:
                flag[j] = 1
        #print(flag)
        cake.sort(key=lambda x: (flag[0]*x[0]-flag[1]*x[1]-flag[2]*x[2]),reverse=True)
        #print(cake)
        tmp = 0
        for j in range(m):
            tmp += abs(cake[j][0])+abs(cake[j][1])+abs(cake[j][2])
        ans = max(ans,tmp)
    print(ans)
