def main():
    S = input()
    min_diff = 1000
    for i in range(len(S)-2):
        X = int(S[i:i+3])
        diff = abs(753 - X)
        if diff < min_diff:
            min_diff = diff
    print(min_diff)

if __name__ == '__main__':
    main()