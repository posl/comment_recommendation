def main():
    S = input()
    S = list(S)
    S = list(map(int, S))
    S.sort()
    if 0 in S:
        print('Yes')
        return
    for i in range(len(S)-2):
        for j in range(i+1, len(S)-1):
            for k in range(j+1, len(S)):
                if (S[i]*100 + S[j]*10 + S[k]) % 8 == 0:
                    print('Yes')
                    return
    print('No')
    return
