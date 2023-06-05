def main():
    n,k,q = map(int,input().split())
    a = list(map(int,input().split()))
    l = list(map(int,input().split()))
    #初始化
    #l中的值对应a中的索引
    #r中的值对应a中的值
    r = [0]*n
    for i in range(k):
        r[a[i]-1] = 1
    #计算每个位置的值
    for i in range(n):
        if r[i] == 0:
            r[i] = r[i-1]
    #计算每个位置的值
    for i in range(q):
        print(r[l[i]-1])
