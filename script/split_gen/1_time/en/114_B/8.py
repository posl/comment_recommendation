def main():
    S = input()
    S = list(S)
    S = [int(i) for i in S]
    #print(S)
    #print(len(S))
    min_diff = 999
    for i in range(len(S)-2):
        X = S[i]*100 + S[i+1]*10 + S[i+2]
        #print(X)
        diff = abs(X - 753)
        if diff < min_diff:
            min_diff = diff
    print(min_diff)
