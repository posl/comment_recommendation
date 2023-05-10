def main():
    # 入力
    s = []
    for i in range(10):
        s.append(input())
    # 処理
    a = 0
    b = 0
    c = 0
    d = 0
    for i in range(10):
        for j in range(10):
            if s[i][j] == '#':
                if a == 0:
                    a = i + 1
                if b < i + 1:
                    b = i + 1
                if c == 0:
                    c = j + 1
                if d < j + 1:
                    d = j + 1
    # 出力
    print(a, b)
    print(c, d)
