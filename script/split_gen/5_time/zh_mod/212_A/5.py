def main():
    # 读取输入
    gold, silver = map(int, input().split())
    # 判断
    if gold == 0:
        if silver == 0:
