def main():
    H, W = map(int, input().split())
    #print(H, W)
    X = [0] * W
    #print(X)
    for i in range(H):
        S = input()
        #print(S)
        for j in range(W):
            if S[j] == "#":
                X[j] += 1
    #print(X)
    print(*X)
