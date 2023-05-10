def main():
    q = int(input())
    a = []
    for i in range(q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            a.append(query[1])
        elif query[0] == 2:
            if len(a) < query[2]:
                print(-1)
            else:
                a.sort()
                print(a[-query[2]])
        elif query[0] == 3:
            if len(a) < query[2]:
                print(-1)
            else:
                a.sort()
                print(a[query[2]-1])
