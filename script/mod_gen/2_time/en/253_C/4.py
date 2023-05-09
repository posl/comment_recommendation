def main():
    Q = int(input())
    S = []
    for _ in range(Q):
        query = list(map(int, input().split()))
        if len(query) == 1:
            print(max(S) - min(S))
        elif len(query) == 2:
            S.append(query[1])
        else:
            for _ in range(min(query[2], S.count(query[1]))):
                S.remove(query[1])

if __name__ == '__main__':
    main()