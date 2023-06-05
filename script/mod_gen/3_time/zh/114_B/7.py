def main():
    S = input()
    S = list(S)
    S = list(map(int, S))
    min_diff = 1000
    for i in range(len(S)-2):
        X = S[i]*100 + S[i+1]*10 + S[i+2]
        diff = abs(X-753)
        if diff < min_diff:
            min_diff = diff
    print(min_diff)

if __name__ == '__main__':
    main()