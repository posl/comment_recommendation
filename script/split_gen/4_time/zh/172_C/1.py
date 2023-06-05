def main():
    #读入数据
    n,m,k = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    #计算前缀和
    a_sum = [0]
    b_sum = [0]
    for i in range(n):
        a_sum.append(a_sum[-1] + a[i])
    for i in range(m):
        b_sum.append(b_sum[-1] + b[i])
    #二分查找
    result = 0
    j = m
    for i in range(n+1):
        if a_sum[i] > k:
            break
        while b_sum[j] > k - a_sum[i]:
            j -= 1
        result = max(result,i+j)
    print(result)
