def main():
    # 读取输入
    a = int(input())
    b = int(input())
    # 用set去重
    print((set([1,2,3]) - set([a,b])).pop())
