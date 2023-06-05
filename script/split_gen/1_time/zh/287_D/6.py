def main():
    S = input()
    T = input()
    len_s = len(S)
    len_t = len(T)
    for x in range(len_t+1):
        if x == 0:
            S_ = S[len_s-len_t:]
        else:
            S_ = S[:x] + S[len_s-len_t+x:]
        flag = True
        for i in range(len_t):
            if T[i] != '?' and T[i] != S_[i]:
                flag = False
                break
        if flag:
            print('Yes')
        else:
            print('No')
