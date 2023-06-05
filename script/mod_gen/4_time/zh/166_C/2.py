def main():
    # 读入数据
    n, m = map(int, input().split())
    h = list(map(int, input().split()))
    # 从1开始编号
    h.insert(0, 0)
    # 用set存储连接关系
    con = set()
    for i in range(m):
        a, b = map(int, input().split())
        con.add((a, b))
        con.add((b, a))
    # 计算好的观测站
    ans = 0
    for i in range(1, n + 1):
        # 遍历所有观测站，如果当前观测站的海拔高于其它观测站，则它是好的
        for j in range(1, n + 1):
            if h[i] <= h[j]:
                break
        else:
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()