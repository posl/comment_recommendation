def main():
    S = input()
    ans = 1000
    for i in range(len(S)-2):
        X = int(S[i:i+3])
        ans = min(ans, abs(753-X))
    print(ans)

if __name__ == '__main__':
    main()