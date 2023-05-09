def main():
    N = int(input())
    N_str = str(N)
    N_len = len(N_str)
    max = 0
    for i in range(1, N_len):
        a = int(N_str[:i])
        b = int(N_str[i:])
        if a*b > max:
            max = a*b
    print(max)
