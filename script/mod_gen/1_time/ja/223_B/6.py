def main():
    S = input()
    N = len(S)
    min_s = S
    max_s = S
    for i in range(N):
        min_s = min(min_s, S[i:] + S[:i])
        max_s = max(max_s, S[i:] + S[:i])
    print(min_s)
    print(max_s)

if __name__ == '__main__':
    main()