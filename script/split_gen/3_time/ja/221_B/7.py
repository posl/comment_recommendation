def main():
    S = input()
    T = input()
    if S == T:
        print('Yes')
    else:
        for i in range(len(S) - 1):
            if S[i] == T[i] and S[i + 1] == T[i + 1]:
                print('Yes')
                return
            if S[i] == T[i + 1] and S[i + 1] == T[i]:
                print('Yes')
                return
        print('No')
