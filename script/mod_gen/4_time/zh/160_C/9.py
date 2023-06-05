def solve(k,n,alist):
    #如果只有一个房子，那么直接返回k
    if n==1:
        return k
    #如果有两个房子，那么返回k-两个房子的距离的最大值
    if n==2:
        return k-max(alist)
    #如果有三个房子，那么返回k-两个房子的距离的最大值
    if n==3:
        return k-max(alist[0]-alist[1],alist[1]-alist[2],alist[2]-alist[0])
    #如果有四个房子，那么返回k-两个房子的距离的最大值
    if n==4:
        return k-max(alist[0]-alist[1],alist[1]-alist[2],alist[2]-alist[3],alist[3]-alist[0])
    #如果有五个房子，那么返回k-两个房子的距离的最大值
    if n==5:
        return k-max(alist[0]-alist[1],alist[1]-alist[2],alist[2]-alist[3],alist[3]-alist[4],alist[4]-alist[0])
    #如果有六个房子，那么返回k-两个房子的距离的最大值
    if n==6:
        return k-max(alist[0]-alist[1],alist[1]-alist[2],alist[2]-alist[3],alist[3]-alist[4],alist[4]-alist[5],alist[5]-alist[0])
    #如果有七个房子，那么返回k-两个房子的距离的最大值
    if n==7:
        return k-max(alist[0]-alist[1],alist[1]-alist[2],alist[2]-alist[3],alist[3]-alist[4],alist[4]-alist[5],alist[5]-alist[6],alist[6]-alist[0])
    #如果有八个房子

if __name__ == '__main__':
    solve()