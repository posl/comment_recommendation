def main():
    S = input()
    Q = int(input())
    query = []
    for _ in range(Q):
        query.append(input().split())
    ans = ""
    for q in query[::-1]:
        if q[0] == "1":
            S = S[::-1]
        else:
            if q[1] == "1":
                S = q[2] + S
            else:
                S = S + q[2]
    print(S)

if __name__ == '__main__':
    main()