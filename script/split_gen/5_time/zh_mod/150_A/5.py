def main():
    # 读取输入
    k, x = map(int, input().split())
    # 判断
    if k * 500 >= x:
        print("Yes")
    else:
