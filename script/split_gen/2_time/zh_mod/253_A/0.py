def main():
    # 读入a, b, c
    a, b, c = map(int, input().split())
    # 判断b是否是中位数
    if a <= b <= c or c <= b <= a:
        print("Yes")
    else:
        print("No")
