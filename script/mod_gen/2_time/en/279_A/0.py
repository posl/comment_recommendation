def main():
    S = input()
    count = 0
    for i in range(len(S)-1):
        if S[i] == 'v' and S[i+1] == 'w':
            count += 1
    print(count)

if __name__ == '__main__':
    main()