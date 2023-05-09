def main():
    S = input()
    S = list(S)
    S = list(map(int, S))
    min = 1000
    for i in range(len(S)-2):
        X = S[i]*100 + S[i+1]*10 + S[i+2]
        if abs(X - 753) < min:
            min = abs(X - 753)
    print(min)
