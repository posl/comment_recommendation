def main():
    S = input()
    N = len(S)
    ans = 999
    for i in range(N-2):
        X = int(S[i:i+3])
        diff = abs(X-753)
        if diff < ans:
            ans = diff
    print(ans)

if __name__ == '__main__':
    main()