def main():
    # 读取输入
    n = int(input())
    l_list = list(map(int, input().split()))
    # 排序
    l_list.sort()
    # 判断
    if l_list[-1] < sum(l_list[:-1]):
        print('是')
    else:
        print('否')
