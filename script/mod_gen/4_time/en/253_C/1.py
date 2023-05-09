def main():
    Q = int(input())
    S = []
    for i in range(Q):
        query = input().split()
        if query[0] == "1":
            S.append(int(query[1]))
        elif query[0] == "2":
            x = int(query[1])
            c = int(query[2])
            for j in range(min(c, S.count(x))):
                S.remove(x)
        else:
            print(max(S)-min(S))

if __name__ == '__main__':
    main()