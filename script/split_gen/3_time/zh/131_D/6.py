def solve():
    n = int(input())
    works = []
    for i in range(n):
        a,b = map(int,input().split())
        works.append((a,b))
    works.sort(key=lambda x:x[1])
    now = 0
    for i in range(n):
        if now + works[i][0] > works[i][1]:
            print("No")
            return
        else:
            now += works[i][0]
    print("Yes")
    return
