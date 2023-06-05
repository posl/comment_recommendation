def main():
    h, w = map(int, input().split())
    s = [input() for _ in range(h)]
    print(s)
    # 从上往下第1行和从左往下第3列的棋子可以通过3步棋到达另一个棋子所在的位置：下、左、左。  由于不可能在两步或更短的时间内做到这一点，所以应该打印3。
