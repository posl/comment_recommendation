def main():
    N = int(input())
    S = []
    for _ in range(N):
        query = list(map(int, input().split()))
        if query[0] == 1:
            S.append(query[1])
        elif query[0] == 2:
            if query[1] in S:
                S.remove(query[1])
        else:
            if len(S) != 0:
                print(max(S)-min(S))

if __name__ == '__main__':
    main()