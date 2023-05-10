def main():
    H, W = map(int, input().split())
    a = [list(input()) for _ in range(H)]
    #print(a)
    #print(a[0][0])
    #print(a[0][1])
    #print(a[1][0])
    #print(a[1][1])
    #print(a[0][0] == a[0][1])
    #print(a[0][0] == a[1][0])
    #print(a[0][0] == a[1][1])
    #print(a[0][1] == a[1][0])
    #print(a[0][1] == a[1][1])
    #print(a[1][0] == a[1][1])
    #print(a[0][0] == a[0][1] == a[1][0] == a[1][1])
    #print(a[0][0] == a[0][1] == a[1][0] == a[1][1])
    #print(a[0][0] == a[0][1] == a[1][0] == a[1][1])
    #print(a[0][0] == a[0][1] == a[1][0] == a[1][1])
    #print(a[0][0] == a[0][1] == a[1][0] == a[1][1])
    #print(a[0][0] == a[0][1] == a[1][0] == a[1][1])
    #print(a[0][0] == a[0][1] == a[1][0] == a[1][1])
    #print(a[0][0] == a[0][1] == a[1][0] == a[1][1])
    #print(a[0][0] == a[0][1] == a[1][0] == a[1][1])
    for i in range(H):
        for j in range(W):
            if a[i][j] == ".":
                if i == 0:
                    if j == 0:
                        if a[i][j] == a[i][j+1] == a[i+1][j] == a[i+1
