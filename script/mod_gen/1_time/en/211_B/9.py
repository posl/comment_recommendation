def main():
    # 4つの文字列を入力
    S = [input() for i in range(4)]
    # 4つの文字列の中にH, 2B, 3B, HRが含まれているかを判定
    if 'H' in S and '2B' in S and '3B' in S and 'HR' in S:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()