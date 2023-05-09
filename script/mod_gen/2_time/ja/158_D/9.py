def main():
    # input
    S = input()
    Q = int(input())
    Query = []
    for i in range(Q):
        Query.append(input().split())
    # compute
    forward = True
    for i in range(Q):
        if Query[i][0] == '1':
            forward = not forward
        elif Query[i][1] == '1':
            if forward:
                S = Query[i][2] + S
            else:
                S = S + Query[i][2]
        else:
            if forward:
                S = S + Query[i][2]
            else:
                S = Query[i][2] + S
    # output
    if forward:
        print(S)
    else:
        print(S[::-1])

if __name__ == '__main__':
    main()