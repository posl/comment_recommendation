def main():
    # 读入数据
    s1 = input()
    s2 = input()
    s3 = input()
    # 列出所有可能的比赛
    all = ["ABC", "ARC", "AGC", "AHC"]
    # 删除已经输入的比赛
    all.remove(s1)
    all.remove(s2)
    all.remove(s3)
    # 打印答案
    print(all[0])
    return
