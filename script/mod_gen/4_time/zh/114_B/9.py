def main():
    S = input()
    S = list(S)
    S = [int(x) for x in S]
    min = 753
    for i in range(len(S)-2):
        X = int(S[i])*100 + int(S[i+1])*10 + int(S[i+2])
        if abs(X-753) < min:
            min = abs(X-753)
    print(min)

if __name__ == '__main__':
    main()