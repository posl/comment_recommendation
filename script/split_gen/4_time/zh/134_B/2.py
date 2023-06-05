def main():
    # 读取输入
    n,d = map(int,input().split())
    # 检查员数量
    count = 0
    # 树列表
    tree = [0 for i in range(n)]
    # 读取树的信息
    for i in range(n):
        tree[i] = int(input())
    # 遍历树
    for i in range(n):
        # 检查员是否已经部署
        flag = False
        # 遍历检查员
        for j in range(count):
            # 检查员已经部署
            if tree[i] - d <= check[j] and check[j] <= tree[i] + d:
                flag = True
                break
        # 检查员未部署
        if flag == False:
            # 部署检查员
            check[count] = tree[i]
            # 检查员数量增加
            count += 1
    # 输出检查员数量
    print(count)
