def main():
    #输入
    N,M = map(int,input().split())
    X = list(map(int,input().split()))
    #排序
    X.sort()
    #求出所有坐标的差值
    diff = []
    for i in range(M-1):
        diff.append(X[i+1] - X[i])
    #按照差值从大到小排序
    diff.sort(reverse=True)
    #求出差值的和
    ans = sum(diff)
    #取出最大的N-1个差值
    ans -= sum(diff[0:N-1])
    #输出
    print(ans)

if __name__ == '__main__':
    main()