def main():
    # 读取输入
    input()
    num_list = input().split(" ")
    # 用集合去重
    num_set = set(num_list)
    # 输出集合元素个数
    print(len(num_set))
