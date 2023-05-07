def main():
    S = input()
    S = list(S)
    S = [int(s) for s in S]
    ans = 999
    for i in range(len(S)-2):
        tmp = int(str(S[i]) + str(S[i+1]) + str(S[i+2]))
        ans = min(ans, abs(tmp - 753))
    print(ans)

if __name__ == '__main__':
    main()