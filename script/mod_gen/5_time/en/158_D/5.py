def main():
    S = input()
    Q = int(input())
    S = list(S)
    reverse = 0
    for i in range(Q):
        query = input().split()
        if query[0] == "1":
            reverse += 1
        else:
            if query[1] == "1":
                if reverse % 2 == 0:
                    S.insert(0, query[2])
                else:
                    S.append(query[2])
            else:
                if reverse % 2 == 0:
                    S.append(query[2])
                else:
                    S.insert(0, query[2])
    if reverse % 2 == 1:
        S.reverse()
    print("".join(S))

if __name__ == '__main__':
    main()