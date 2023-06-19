def main():
    # 读取输入
    s,w = map(int,input().split())
    # 判断
    if s <= w:
        print("不安全")
    else:
        print("安全")
