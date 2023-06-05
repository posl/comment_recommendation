def main():
    S = input()
    T = input()
    S_len = len(S)
    T_len = len(T)
    # print(S_len)
    # print(T_len)
    min = 1000
    for i in range(S_len-T_len+1):
        # print(i)
        # print(S[i:i+T_len])
        count = 0
        for j in range(T_len):
            if S[i+j] != T[j]:
                count += 1
        if count < min:
            min = count
    print(min)

if __name__ == '__main__':
    main()