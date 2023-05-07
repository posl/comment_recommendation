def main():
    H, W = map(int, input().split())
    S = []
    for _ in range(H):
        S.append(input())
    
    for i in range(H):
        for j in range(W):
            if S[i][j] == "o":
                X = i
                Y = j
    
    X += 1
    Y += 1
    
    print(max(X, Y, H-X+1, W-Y+1)-1)
