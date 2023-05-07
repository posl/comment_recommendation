def main():
    S, K = input().split()
    K = int(K)
    S = sorted(list(S))
    ans = []
    while S:
        i = 0
        while i < len(S):
            if i == 0:
                tmp = 1
            else:
                tmp *= i
            if tmp >= K:
                ans.append(S[i])
                S.pop(i)
                K -= (tmp // i)
                break
            i += 1
    print(''.join(ans))

if __name__ == '__main__':
    main()