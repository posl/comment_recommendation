def main():
    # 读取输入
    a,b = map(int,input().split())
    # 处理
    if b % a == 0:
        print(a+b)
    else:
        print(b-a)
