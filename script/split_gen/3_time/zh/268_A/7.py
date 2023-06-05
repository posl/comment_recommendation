def main():
    # 读取输入
    a,b,c,d,e = map(int, input().split())
    # 用set去重
    l = [a,b,c,d,e]
    print(len(set(l)))
