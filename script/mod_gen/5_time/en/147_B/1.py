def main():
    S = input()
    count = 0
    for i in range(len(S)//2):
        if S[i] != S[len(S)-i-1]:
            count += 1
    print(count)

if __name__ == '__main__':
    main()