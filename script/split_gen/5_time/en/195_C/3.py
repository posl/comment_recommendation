def main():
    N = int(input())
    N_str = str(N)
    N_len = len(N_str)
    if N_len <= 3:
        print(0)
        return
    comma_num = (N_len - 1) // 3
    if (N_len - 1) % 3 == 0:
        comma_num -= 1
    comma_num += (N_len - 1) % 3
    print(comma_num)
