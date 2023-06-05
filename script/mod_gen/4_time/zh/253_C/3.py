def main():
    Q = int(input())
    S = []
    for i in range(Q):
        query = input().split()
        if query[0] == '1':
            S.append(int(query[1]))
        elif query[0] == '2':
            x = int(query[1])
            c = int(query[2])
            if x in S:
                count = 0
                for j in range(len(S)):
                    if S[j] == x:
                        S.pop(j)
                        count += 1
                        if count == c:
                            break
        elif query[0] == '3':
            print(max(S) - min(S))

if __name__ == '__main__':
    main()