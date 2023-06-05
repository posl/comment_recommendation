def main():
    # 读取输入
    input_line = input().split()
    # 初始化一个空列表
    list = []
    # 遍历输入的每一个值
    for i in range(len(input_line)):
        # 将每一个值转换为int类型，并添加到列表中
        list.append(int(input_line[i]))
    # 将列表转换为集合，并打印集合的长度
    print(len(set(list)))
