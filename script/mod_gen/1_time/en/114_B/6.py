def main():
    S = input()
    S = [int(c) for c in S]
    min_diff = 1000
    for i in range(len(S)-2):
        X = S[i] * 100 + S[i+1] * 10 + S[i+2]
        diff = abs(753 - X)
        if diff < min_diff:
            min_diff = diff
    print(min_diff)

if __name__ == '__main__':
    main()