def main():
    # 读取数据
    n = int(input())
    a = list(map(int, input().split()))
    # set函数去重
    if len(set(a)) == len(a):
        print("Yes")
    else:
        print("No")
