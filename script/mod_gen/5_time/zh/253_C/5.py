def main():
    Q = int(input())
    S = []
    for i in range(Q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            S.append(query[1])
        elif query[0] == 2:
            for j in range(query[2]):
                if query[1] in S:
                    S.remove(query[1])
                else:
                    break
        elif query[0] == 3:
            S.sort()
            print(S[-1]-S[0])

if __name__ == '__main__':
    main()