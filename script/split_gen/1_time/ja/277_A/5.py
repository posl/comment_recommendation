def main():
    N, X = map(int, input().split())
    P = list(map(int, input().split()))
    #Xの位置を求める
    for i in range(N):
        if P[i] == X:
            print(i + 1)
            break
