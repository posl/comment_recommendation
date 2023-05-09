def main():
    q = int(input())
    a = []
    for i in range(q):
        query = list(map(int,input().split()))
        if query[0] == 1:
            a.append(query[1])
        elif query[0] == 2:
            a.sort()
            a = list(reversed(a))
            if len(a) >= query[2]:
                print(a[query[2]-1])
            else:
                print(-1)
        else:
            a.sort()
            if len(a) >= query[2]:
                print(a[query[2]-1])
            else:
                print(-1)
