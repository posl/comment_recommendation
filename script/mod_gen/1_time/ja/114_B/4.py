def main():
    S = input()
    min = 753
    for i in range(len(S)-2):
        if abs(753-int(S[i:i+3])) < min:
            min = abs(753-int(S[i:i+3]))
    print(min)

if __name__ == '__main__':
    main()