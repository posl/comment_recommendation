def main():
    n = input()
    n = int(n)
    n_str = str(n)
    n_len = len(n_str)
    if n_len == 1:
        if n % 3 == 0:
            print(0)
        else:
            print(-1)
    else:
        sum_n = 0
        for i in range(n_len):
            sum_n += int(n_str[i])
        if sum_n % 3 == 0:
            print(0)
        elif sum_n % 3 == 1:
            if '1' in n_str:
                if n_len == 2:
                    print(-1)
                elif '2' in n_str:
                    print(1)
                else:
                    print(2)
            else:
                if n_len == 2:
                    print(-1)
                else:
                    print(2)
        else:
            if '2' in n_str:
                if n_len == 2:
                    print(-1)
                elif '1' in n_str:
                    print(1)
                else:
                    print(2)
            else:
                if n_len == 2:
                    print(-1)
                else:
                    print(2)
