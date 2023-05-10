def main():
    S = input()
    K = int(input())
    S = S.replace('X', '0').replace('.', '1')
    S = S.split('0')
    S = [len(s) for s in S]
    S = [s - 1 for s in S if s > 0]
    S = [0] + S + [0]
    for i in range(len(S) - 1):
        S[i + 1] += S[i]
    ans = 0
    for i in range(0, len(S), 2):
        if i + 2 * K + 1 < len(S):
            ans = max(ans, S[i + 2 * K + 1] - S[i])
        else:
            ans = max(ans, S[-1] - S[i])
    print(ans)

if __name__ == '__main__':
    main()