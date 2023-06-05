def main():
    x = int(input())
    if 0 <= x <= 100000:
        print(100 - x % 100)
    else:
        print("输入错误")
