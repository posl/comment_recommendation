def main():
    S = input()
    for i in range(0, len(S)):
        if S.count(S[i]) == 1:
            print(S[i])
            break
        if i == len(S)-1:
            print("-1")

if __name__ == '__main__':
    main()