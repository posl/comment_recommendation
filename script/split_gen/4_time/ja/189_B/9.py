def main():
    N,X = map(int,input().split())
    VPs = [list(map(int,input().split())) for _ in range(N)]
    alc = 0
    for i in range(N):
        alc += VPs[i][0] * VPs[i][1] / 100
        if alc > X:
            print(i+1)
            return
    print(-1)
