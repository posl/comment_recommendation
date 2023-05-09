def main():
    S = input()
    T = input()
    for i in range(len(T)+1):
        S_ = S[:i] + S[len(S)-len(T)+i:]
        if S_.replace('?', '') == T:
            print('Yes')
        else:
            print('No')
