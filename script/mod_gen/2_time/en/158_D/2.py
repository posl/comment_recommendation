def main():
    S = input()
    Q = int(input())
    rev = False
    for _ in range(Q):
        query = list(input().split())
        if len(query) == 1:
            rev = not rev
        else:
            if query[1] == '1':
                if rev:
                    S = S + query[2]
                else:
                    S = query[2] + S
            else:
                if rev:
                    S = query[2] + S
                else:
                    S = S + query[2]
    if rev:
        S = S[::-1]
    print(S)

if __name__ == '__main__':
    main()