def main():
    # 读取输入
    n = int(input())
    # 判断是否包含数字7
    if n % 10 == 7 or n // 10 % 10 == 7 or n // 100 == 7:
        print("Yes")
