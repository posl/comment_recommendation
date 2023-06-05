def main():
    N,X,Y,Z = map(int,input().split())
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    score = []
    for i in range(N):
        score.append([A[i]+B[i],A[i],B[i],i+1])
    score.sort(reverse=True)
    for i in range(X):
        print(score[i][3])
    for i in range(X,X+Y):
        print(score[i][3])
    for i in range(X+Y,X+Y+Z):
        print(score[i][3])
