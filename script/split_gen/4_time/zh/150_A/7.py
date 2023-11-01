def main():
    # 读取输入
    k, x = map(int, input().split())
    # 处理
    if k * 500 >= x:
        result = 'Yes'
