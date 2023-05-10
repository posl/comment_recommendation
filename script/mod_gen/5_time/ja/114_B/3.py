def main():
    S = input()
    min_diff = 999
    for i in range(0,len(S)-2):
        X = int(S[i:i+3])
        diff = abs(X-753)
        if diff < min_diff:
            min_diff = diff
    print(min_diff)

if __name__ == '__main__':
    main()