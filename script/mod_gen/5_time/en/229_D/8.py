def main():
    S = input()
    K = int(input())
    S = S.replace('X','.')
    S = S.split('.')
    S = list(map(len, S))
    S = list(map(lambda x: x - 1, S))
    for i in range(len(S)):
        if K > 0:
            if S[i] > 0:
                if K >= S[i]:
                    K -= S[i]
                    S[i] += 1
                else:
                    S[i] += K
                    K = 0
    print(max(S))

if __name__ == '__main__':
    main()