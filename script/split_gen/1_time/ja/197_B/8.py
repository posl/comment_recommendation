def main():
    H,W,X,Y = map(int,input().split())
    S = [input() for i in range(H)]
    count = 0
    for i in range(X-1):
        if S[X-2-i][Y-1] == '#':
            break
        else:
            count += 1
    for i in range(H-X):
        if S[X+i][Y-1] == '#':
            break
        else:
            count += 1
    for i in range(Y-1):
        if S[X-1][Y-2-i] == '#':
            break
        else:
            count += 1
    for i in range(W-Y):
        if S[X-1][Y+i] == '#':
            break
        else:
            count += 1
    print(count+1)
