def main():
    N = int(input())
    if N == 0:
        print(0)
        return
    if N == 1:
        print(2)
        return
    # 1^3 + 1^2 + 1 + 1 = 4
    # 2^3 + 2^2 + 2 + 2 = 12
    # 3^3 + 3^2 + 3 + 3 = 36
    # 4^3 + 4^2 + 4 + 4 = 80
    # 5^3 + 5^2 + 5 + 5 = 150
    # 6^3 + 6^2 + 6 + 6 = 252
    # 7^3 + 7^2 + 7 + 7 = 392
    # 8^3 + 8^2 + 8 + 8 = 576
    # 9^3 + 9^2 + 9 + 9 = 810
    # 10^3 + 10^2 + 10 + 10 = 1100
    # 11^3 + 11^2 + 11 + 11 = 1452
    # 12^3 + 12^2 + 12 + 12 = 1872
    # 13^3 + 13^2 + 13 + 13 = 2366
    # 14^3 + 14^2 + 14 + 14 = 2940
    # 15^3 + 15^2 + 15 + 15 = 3600
    # 16^3 + 16^2 + 16 + 16 = 4352
    # 17^3 + 17^2 + 17 + 17 = 5202
    # 18^3 + 18^2 + 18 + 18 = 6160
    # 19^3 + 19^2 + 19 + 19 = 7236
    # 20^3 + 20^2 + 20 + 20 = 8440
    # 21^3 + 21^2 + 21 + 21 = 9782
    # 22^3 + 22