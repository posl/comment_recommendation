def main():
    S = input()
    S_min = S
    S_max = S
    for i in range(len(S)):
        S = S[1:] + S[0]
        if S_min > S:
            S_min = S
        if S_max < S:
            S_max = S
    print(S_min)
    print(S_max)

if __name__ == '__main__':
    main()