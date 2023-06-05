def main():
    #读取数据
    n,a,b = map(int,input().split())
    p,q,r,s = map(int,input().split())
    #初始化
    #矩阵
    matrix = [['.' for i in range(n)] for j in range(n)]
    #计算最大最小值
    min1 = min(1-a,1-b)
    max1 = max(n-a,n-b)
    min2 = min(1-a,b-n)
    max2 = max(n-a,b-1)
    #对矩阵进行填充
    for i in range(min1,max1+1):
        matrix[a+i-1][b+i-1] = '#'
    for i in range(min2,max2+1):
        matrix[a+i-1][b-i-1] = '#'
    #输出结果
    for i in range(p-1,q):
        print(''.join(matrix[i][r-1:s]))
