def main():
    n,m = map(int,input().split())
    b = []
    for _ in range(n):
        b.append(list(map(int,input().split())))
    for i in range(1,n):
        for j in range(1,m):
            if b[i][j] != b[i-1][j-1] + 7:
                print("No")
                return
    print("Yes")
