def main():
    n = int(input())
    n_str = str(n)
    n_len = len(n_str)
    if n_len <= 3:
        print(0)
    else:
        if n_len % 3 == 0:
            print((n_len - 1) // 3)
        else:
            print((n_len - 1) // 3 + 1)

if __name__ == '__main__':
    main()