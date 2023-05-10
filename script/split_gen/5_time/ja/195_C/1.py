def main():
    N = int(input())
    N_str = str(N)
    N_len = len(N_str)
    if N_len <= 3:
        print(0)
        return
    if N_len % 3 == 0:
        print((N_len // 3) - 1)
    else:
        print(N_len // 3)
