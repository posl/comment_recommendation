def main():
    Q = int(input())
    S = []
    for i in range(0,Q):
        query = input().split()
        if query[0] == '1':
            S.append(int(query[1]))
        elif query[0] == '2':
            x = int(query[1])
            c = int(query[2])
            for j in range(0,c):
                if x in S:
                    S.remove(x)
                else:
                    break
        else:
            print(max(S)-min(S))

if __name__ == '__main__':
    main()