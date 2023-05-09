def main():
    # 水圧は水深のみに依存し、水深 x [m] の場所では (x/(100)) [MPa] になるものとします。
    # 水深 D [m] の場所の水圧は何 [MPa] ですか？
    d = int(input())
    print(d/100)
