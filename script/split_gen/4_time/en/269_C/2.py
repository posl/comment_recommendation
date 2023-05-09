def main():
    N = int(input())
    N_bin = bin(N)[2:]
    N_len = len(N_bin)
    N_1 = [i for i in range(N_len) if N_bin[i] == "1"]
    max_x = 2**len(N_1)
    for i in range(max_x):
        x_bin = bin(i)[2:]
        x_len = len(x_bin)
        x_1 = [i for i in range(x_len) if x_bin[i] == "1"]
        if set(x_1).issubset(N_1):
            print(i)
