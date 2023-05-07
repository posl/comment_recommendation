def main():
    S = input()
    for i in range(0, len(S)-1):
        print(S[i], end='')
    print(S[len(S)-1])

if __name__ == '__main__':
    main()