def main():
    S = input()
    T = input()
    # 文字列をソートしたものを比較
    S_sort = sorted(S)
    T_sort = sorted(T)
    if S_sort == T_sort:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()