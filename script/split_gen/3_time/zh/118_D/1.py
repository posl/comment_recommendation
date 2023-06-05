def main():
    #输入
    n,m = map(int, input().split())
    a = list(map(int, input().split()))
    #将a中的数字和对应的数字放入字典中
    d = dict()
    for i in range(m):
        d[a[i]] = i+1
    #按照数字的从大到小的顺序排列
    a.sort(reverse=True)
    #用最大的数字填充
    ans = ""
    for i in range(m):
        ans += str(a[i]) * (n // a[i])
        n %= a[i]
    #如果n不为0，则说明没有数字可以填充，输出-1
    if n != 0:
        print(-1)
    else:
        print(ans)
