def main():
    S = input()
    S = list(S)
    count = 0
    for i in range(len(S)):
        if i%2 == 0:
            if S[i] == '0':
                count += 1
        else:
            if S[i] == '1':
                count += 1
    print(min(count, len(S)-count))

if __name__ == '__main__':
    main()