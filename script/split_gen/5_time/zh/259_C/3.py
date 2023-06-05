def main():
    S = input()
    T = input()
    S_len = len(S)
    T_len = len(T)
    if S_len >= 2 and S_len <= 2*10**5 and T_len >= 2 and T_len <= 2*10**5:
        if S == T:
            print("Yes")
        else:
            for i in range(S_len-1):
                if S[i] == S[i+1]:
                    S = S[0:i+1] + S[i] + S[i+1:]
                    if S == T:
                        print("Yes")
                        break
                    else:
                        print("No")
    else:
        print("No")
