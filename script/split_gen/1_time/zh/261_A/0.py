def main():
    # 读取输入
    l1,r1,l2,r2 = map(int,input().split())
    # 求解
    if r1 < l2 or r2 < l1:
        # 没有重叠
        print(0)
    else:
        # 有重叠
        print(min(r1,r2)-max(l1,l2))
