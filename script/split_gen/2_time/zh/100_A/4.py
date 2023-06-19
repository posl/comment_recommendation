def main():
    # 读入数据
    a,b = map(int,input().split())
    # 检查是否满足条件
    if a <= 8 and b <= 8:
        print('Yay!')
    else:
        print(':(')
