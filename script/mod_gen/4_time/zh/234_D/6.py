def main():
    n,k = map(int,input().split())
    p = list(map(int,input().split()))
    # 遍历p，找到前k个最大值，存入res
    res = []
    for i in range(k-1,n):
        max = p[i]
        for j in range(i-k+1,i):
            if max < p[j]:
                max = p[j]
        res.append(max)
    # 输出res
    for i in range(len(res)):
        print(res[i])

if __name__ == '__main__':
    main()