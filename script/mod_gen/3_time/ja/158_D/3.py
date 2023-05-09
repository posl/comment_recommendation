def main():
    S = input()
    Q = int(input())
    query = [input().split() for _ in range(Q)]
    ans = []
    for i in range(Q):
        if query[i][0] == "1":
            query = query[::-1]
        else:
            if query[i][1] == "1":
                ans.append(query[i][2])
            else:
                ans.append(query[i][2])
    ans = "".join(ans)
    if query[0][0] == "1":
        ans = ans[::-1]
    ans = ans + S
    print(ans)

if __name__ == '__main__':
    main()