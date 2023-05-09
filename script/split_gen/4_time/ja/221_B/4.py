def main():
    S = input()
    T = input()
    if S == T:
        print('Yes')
    else:
        for i in range(len(S)-1):
            if S[i+1] == T[i] and S[i] == T[i+1]:
                print('Yes')
                exit()
        print('No')
