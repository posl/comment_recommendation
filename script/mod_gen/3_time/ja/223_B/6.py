def main():
    # input
    S = input()
    # compute
    S_min = S
    S_max = S
    for i in range(len(S)):
        S = S[1:] + S[0]
        S_min = min(S_min, S)
        S_max = max(S_max, S)
    # output
    print(S_min)
    print(S_max)

if __name__ == '__main__':
    main()