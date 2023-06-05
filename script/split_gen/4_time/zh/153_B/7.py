def main():
    # 读取输入
    H, N = map(int, input().split())
    A = list(map(int, input().split()))
    # 一开始是不行的
    can = False
    # 从大到小排序
    A.sort(reverse=True)
    # 从大到小循环
    for a in A:
        # 如果H小于a，那么就是不行的
        if H <= a:
            can = True
            break
        # 如果H大于a，那么就减去a
        else:
            H -= a
    # 打印结果
    if can:
        print("Yes")
    else:
        print("No")
