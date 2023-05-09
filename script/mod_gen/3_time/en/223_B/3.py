def main():
    S = input()
    S_len = len(S)
    S_min = S
    S_max = S
    for i in range(S_len):
        S = S[-1] + S[:-1]
        if S < S_min:
            S_min = S
        if S > S_max:
            S_max = S
    print(S_min)
    print(S_max)

if __name__ == '__main__':
    main()