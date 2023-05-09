def main():
    S = input()
    S = [int(s) for s in S]
    ans = 10**10
    for i in range(len(S) - 2):
        ans = min(ans, abs(753 - (S[i] * 100 + S[i + 1] * 10 + S[i + 2])))
    print(ans)

if __name__ == '__main__':
    main()