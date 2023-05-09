def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    # Kの2進数表記を求める
    k_bin = bin(K)[2:]
    # 2進数表記の桁数を求める
    k_len = len(k_bin)
    # 2進数表記の桁数のうち、0の桁数を求める
    zero_num = k_bin.count('0')
    # 2進数表記の桁数のうち、1の桁数を求める
    one_num = k_len - zero_num
    # 2進数表記の桁数のうち、1の桁数を求める
    one_num = k_len - zero_num
    # 2進数表記の桁数のうち、0の桁数を求める
    zero_num = k_bin.count('0')
    # Kの2進数表記を求める
    k_bin = bin(K)[2:]
    # 2進数表記の桁数を求める
    k_len = len(k_bin)
    # 2進数表記の桁数のう

if __name__ == '__main__':
    main()