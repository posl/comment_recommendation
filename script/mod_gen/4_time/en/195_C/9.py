def main():
    N = int(input())
    N_str = str(N)
    N_len = len(N_str)
    N_comma = int((N_len-1)/3)
    N_comma_total = N_comma * 2
    if N_len % 3 == 0:
        N_comma_total += 1
    elif N_len % 3 == 1:
        N_comma_total += 1
    elif N_len % 3 == 2:
        N_comma_total += 2
    print(N_comma_total)

if __name__ == '__main__':
    main()