def main():
    Q = int(input())
    S = []
    for _ in range(Q):
        query = input().split()
        if query[0] == "1":
            S.append(int(query[1]))
        elif query[0] == "2":
            x = int(query[1])
            c = int(query[2])
            m = min(c, S.count(x))
            for _ in range(m):
                S.remove(x)
        else:
            print(max(S)-min(S))

if __name__ == '__main__':
    main()