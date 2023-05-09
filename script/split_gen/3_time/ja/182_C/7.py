def main():
    N = int(input())
    # 3の倍数を作ることができるか
    # 3の倍数を作るのに必要な最少の消す桁数を求める
    N_str = str(N)
    N_len = len(N_str)
    N_sum = sum(map(int, N_str))
    if N_sum % 3 == 0:
        print(0)
    elif N_len == 1:
        print(-1)
    elif N_sum % 3 == 1:
        if N_len == 2:
            if N_str[0] == '1' or N_str[1] == '1':
                print(1)
            else:
                print(-1)
        else:
            if N_str.count('1') >= 1 or N_str.count('4') >= 1 or N_str.count('7') >= 1:
                print(1)
            elif N_str.count('2') >= 2 or N_str.count('5') >= 2 or N_str.count('8') >= 2:
                print(2)
            else:
                print(-1)
    else:
        if N_len == 2:
            if N_str[0] == '2' or N_str[1] == '2':
                print(1)
            else:
                print(-1)
        else:
            if N_str.count('2') >= 1 or N_str.count('5') >= 1 or N_str.count('8') >= 1:
                print(1)
            elif N_str.count('1') >= 2 or N_str.count('4') >= 2 or N_str.count('7') >= 2:
                print(2)
            else:
                print(-1)
