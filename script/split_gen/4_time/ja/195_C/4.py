def main():
    N = int(input())
    N_len = len(str(N))
    if N_len <= 3:
        print(0)
    else:
        if N_len % 3 == 0:
            print((N_len // 3) - 1)
        else:
            print(N_len // 3)
