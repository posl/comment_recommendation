def main():
    S = input()
    X = []
    for i in range(len(S)-2):
        X.append(abs(753-int(S[i:i+3])))
    print(min(X))

if __name__ == '__main__':
    main()