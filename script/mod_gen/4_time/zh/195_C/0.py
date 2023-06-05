def main():
    n = int(input())
    n_str = str(n)
    n_len = len(n_str)
    # 1~999
    if n_len <= 3:
        print(0)
        return
    # 1000~999999
    elif 3 < n_len <= 6:
        print(n_len - 3)
        return
    # 1000000~999999999
    elif 6 < n_len <= 9:
        print((n_len - 3) * 2 + 3)
        return
    # 1000000000~999999999999
    elif 9 < n_len <= 12:
        print((n_len - 3) * 3 + 3)
        return
    # 1000000000000~999999999999999
    elif 12 < n_len <= 15:
        print((n_len - 3) * 4 + 3)
        return
    # 1000000000000000~999999999999999999
    elif 15 < n_len <= 18:
        print((n_len - 3) * 5 + 3)
        return
    # 1000000000000000000~999999999999999999999
    elif 18 < n_len <= 21:
        print((n_len - 3) * 6 + 3)
        return
    # 1000000000000000000000~999999999999999999999999
    elif 21 < n_len <= 24:
        print((n_len - 3) * 7 + 3)
        return
    # 1000000000000000000000000~999999999999999999999999999
    elif 24 < n_len <= 27:
        print((n_len - 3) * 8 + 3)
        return
    # 1000000000000000000

if __name__ == '__main__':
    main()