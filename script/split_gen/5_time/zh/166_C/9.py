def main():
    n,m = map(int,input().split())
    h = list(map(int,input().split()))
    a = []
    b = []
    for i in range(m):
        a1,b1 = map(int,input().split())
        a.append(a1)
        b.append(b1)
    #print(n,m,h,a,b)
    #创建一个n*n的矩阵，用于存储各个节点之间的关系
    #0表示不通，1表示通
    #c = [[0 for i in range(n)] for j in range(n)]
    c = [[0]*n for i in range(n)]
    for i in range(m):
        c[a[i]-1][b[i]-1] = 1
        c[b[i]-1][a[i]-1] = 1
    #print(c)
    #遍历每个节点，判断是否满足条件
    #如果满足条件，则该节点为好的观测站
    #如果不满足条件，则该节点不是好的观测站
    #计算每个节点的海拔高度
    #找到所有节点中的最大海拔高度
    #maxh = max(h)
    #print(maxh)
    #print(h)
    #print(max(h))
    #创建一个空列表，用于存储好的观测站
    g = []
    for i in range(n):
        #print(i)
        #print(h[i])
        #print(max(h))
        #如果当前节点的海拔高度大于所有节点中的最大海拔高度
        #则该节点为好的观测站
        #如果当前节点的海拔高度小于所有节点中的最大海拔高度
        #则该节点不是好的观测站
        if h[i] >= max(h):
            #print('good')
            g.append(i)
        else:
            #print('bad')
            pass
    #print(g)
    #print(len(g))
    #判断好的观测站的个数
    #如果只有一个好的观测站，那
