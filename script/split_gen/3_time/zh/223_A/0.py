def main():
    # 读入数据
    x = int(input())
    # 检查是否满足条件
    if 0 <= x <= 1000 and x % 100 == 0:
        print("Yes")
    else:
        print("No")
