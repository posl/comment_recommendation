def main():
    # 读入数据
    X, Y, Z, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))
    # 从大到小排序
    A.sort(reverse=True)
    B.sort(reverse=True)
    C.sort(reverse=True)
    # 暴力搜索
    ans = []
    for a in A:
        for b in B:
            for c in C:
                ans.append(a + b + c)
    # 从大到小排序
    ans.sort(reverse=True)
    # 打印前K个
    for i in range(K):
        print(ans[i])

if __name__ == '__main__':
    main()