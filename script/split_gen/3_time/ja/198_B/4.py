def main():
    N = int(input())
    N_str = str(N)
    N_str_reverse = N_str[::-1]
    if N_str == N_str_reverse:
        print("Yes")
    else:
        print("No")
