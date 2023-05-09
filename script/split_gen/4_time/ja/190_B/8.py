def solve():
    n,s,d = map(int,input().split())
    magic = []
    for i in range(n):
        magic.append(list(map(int,input().split())))
    for i in range(n):
        if magic[i][0] < s and magic[i][1] > d:
            print("Yes")
            return
    print("No")
    return
