def main():
    s = input()
    q = int(input())
    query = []
    for i in range(q):
        query.append(input().split())
    s = list(s)
    f = 0
    for i in range(q):
        if query[i][0] == "1":
            if f == 0:
                f = 1
            else:
                f = 0
        else:
            if query[i][1] == "1":
                if f == 0:
                    s.insert(0, query[i][2])
                else:
                    s.append(query[i][2])
            else:
                if f == 0:
                    s.append(query[i][2])
                else:
                    s.insert(0, query[i][2])
    if f == 0:
        print("".join(s))
    else:
        s.reverse()
        print("".join(s))
main()
