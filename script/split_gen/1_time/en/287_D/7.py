def main():
    S = input()
    T = input()
    for x in range(len(T)+1):
        S1 = S[0:x]
        S2 = S[len(S)-len(T)+x:]
        if S1.count('?') + S2.count('?') + len(T) == len(S):
            for i in range(len(T)):
                if S1[i] != T[i] and S1[i] != '?':
                    break
                if S2[i] != T[i] and S2[i] != '?':
                    break
            else:
                print('Yes')
                continue
        print('No')
    return
