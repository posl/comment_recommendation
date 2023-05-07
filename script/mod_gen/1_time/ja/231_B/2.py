def main():
    N = int(input())
    S = []
    for i in range(N):
        S.append(input())
    S_set = set(S)
    S_count = []
    for i in S_set:
        S_count.append(S.count(i))
    print(S[S_count.index(max(S_count))])

if __name__ == '__main__':
    main()