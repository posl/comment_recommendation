def main():
    # Input
    S = input()
    # Constants
    MOD = 10**9 + 7
    # Main Logic
    if len(S) < 8:
        print(0)
        return
    # 8文字を選ぶ場合の数
    # 8C1 + 8C2 + 8C3 + 8C4 + 8C5 + 8C6 + 8C7 + 8C8
    # 8! / (1! * 7!) + 8! / (2! * 6!) + 8! / (3! * 5!) + 8! / (4! * 4!) + 8! / (5! * 3!) + 8! / (6! * 2!) + 8! / (7! * 1!) + 8! / (8! * 0!)
    # 8! / (1! * 7!) + 8! / (2! * 6!) + 8! / (3! * 5!) + 8! / (4! * 4!) + 8! / (5! * 3!) + 8! / (6! * 2!) + 8! / (7! * 1!) + 8! / 1
    # 8! / 7! + 8! / 6! + 8! / 5! + 8! / 4! + 8! / 3! + 8! / 2! + 8! / 1! + 8! / 1
    # 8 * 7 * 6 * 5 * 4 * 3 * 2 * 1 / 7 * 6 * 5 * 4 * 3 * 2 * 1 * 1
    # 8 * 7 * 6 * 5 * 4 * 3 * 2 / 7 * 6 * 5 * 4 * 3 * 2 * 1
    # 8 * 7 * 6 * 5 * 4 * 3 * 2 / 1 * 1 * 1 * 1 * 1 * 1 * 1
    #

if __name__ == '__main__':
    main()