def main():
    # A = 収縮期血圧
    # B = 拡張期血圧
    A, B = map(int, input().split())
    # 平均血圧 = (収縮期血圧 - 拡張期血圧) / 3 + 拡張期血圧
    C = ((A - B) / 3) + B
    print(C)
