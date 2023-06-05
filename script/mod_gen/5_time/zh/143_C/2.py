def main():
    N = int(input())
    S = input()
    S = list(S)
    i = 0
    while i < len(S)-1:
        if S[i] == S[i+1]:
            del S[i+1]
            i -= 1
        else:
            i += 1
    print(len(S))

if __name__ == '__main__':
    main()