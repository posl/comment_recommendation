def main():
    Q = int(input())
    S = []
    for _ in range(Q):
        query = list(map(int,input().split()))
        if query[0] == 1:
            S.append(query[1])
        elif query[0] == 2:
            for i in range(query[2]):
                if query[1] in S:
                    S.remove(query[1])
        else:
            print(max(S)-min(S))

if __name__ == '__main__':
    main()