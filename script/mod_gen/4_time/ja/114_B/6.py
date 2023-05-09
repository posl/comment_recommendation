def main():
    S = input()
    result = 999
    for i in range(len(S)-2):
        X = int(S[i:i+3])
        result = min(result, abs(753 - X))
    print(result)

if __name__ == '__main__':
    main()