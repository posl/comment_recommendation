def main():
    # 读取输入
    int_list = list(map(int, input().split()))
    # 用set去重
    int_set = set(int_list)
    # 打印答案
    print(len(int_set))
