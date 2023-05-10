def main():
    S = input()
    T = input()
    s_len = len(S)
    t_len = len(T)
    for i in range(t_len):
        if S[s_len - t_len + i] != T[i] and S[s_len - t_len + i] != '?':
            print('No')
            return
    print('Yes')
main()

if __name__ == '__main__':
    main()