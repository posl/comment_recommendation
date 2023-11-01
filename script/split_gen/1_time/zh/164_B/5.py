def main():
    # 读取输入
    a, b, c, d = map(int, input().split())
    # 一直战斗直到有一方死亡
    while True:
        # 高桥的怪物攻击青木的怪物
        c -= b
        #
