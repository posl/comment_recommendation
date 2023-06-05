def main():
    #读取输入
    N = int(input())
    #print(N)
    #初始化数组
    t = [0]*N
    l = [0]*N
    r = [0]*N
    #print(t,l,r)
    #循环读取
    for i in range(N):
        t[i],l[i],r[i] = map(int,input().split())
    #print(t,l,r)
    #计算
    count = 0
    for i in range(N-1):
        for j in range(i+1,N):
            if (l[i]<=l[j] and l[j]<=r[i]) or (l[i]<=r[j] and r[j]<=r[i]) or (l[j]<=l[i] and l[i]<=r[j]) or (l[j]<=r[i] and r[i]<=r[j]):
                count += 1
    #输出
    print(count)
