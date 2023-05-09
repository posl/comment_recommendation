def main():
    n,m = map(int,input().split())
    ab = []
    cd = []
    for i in range(m):
        ab.append(list(map(int,input().split())))
    for i in range(m):
        cd.append(list(map(int,input().split())))
    ab.sort()
    cd.sort()
    for i in range(m):
        if ab[i] != cd[i]:
            print("No")
            break
        if i == m-1:
            print("Yes")
