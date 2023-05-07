def main():
    S = input()
    N = len(S)
    S_min = S
    S_max = S
    for i in range(N):
        S_min = min(S_min, S[i:] + S[:i])
        S_max = max(S_max, S[i:] + S[:i])
    print(S_min)
    print(S_max)

if __name__ == '__main__':
    main()