def main():
    S = input()
    T = input()
    if S == T:
        print('Yes')
    else:
        for i in range(len(S)):
            if S[i] != T[i]:
                tmp = S[i]
                S = S[:i] + S[i+1]
                S = S[:i+1] + tmp + S[i+1:]
                if S == T:
                    print('Yes')
                    break
                else:
                    print('No')
                    break
