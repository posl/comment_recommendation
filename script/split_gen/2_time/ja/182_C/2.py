def main():
    N = int(input())
    N_str = str(N)
    N_len = len(N_str)
    N_sum = sum(map(int, N_str))
    if N_sum % 3 == 0:
        print(0)
    elif N_sum % 3 == 1:
        if N_str.count("1") >= 1:
            print(1)
        elif N_str.count("4") >= 1:
            print(1)
        elif N_str.count("7") >= 1:
            print(1)
        else:
            if N_len <= 2:
                print(-1)
            else:
                print(2)
    else:
        if N_str.count("2") >= 1:
            print(1)
        elif N_str.count("5") >= 1:
            print(1)
        elif N_str.count("8") >= 1:
            print(1)
        else:
            if N_len <= 2:
                print(-1)
            else:
                print(2)
