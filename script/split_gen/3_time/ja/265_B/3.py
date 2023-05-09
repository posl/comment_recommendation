def main():
    N, M, T = map(int, input().split())
    A = list(map(int, input().split()))
    XY = [list(map(int, input().split())) for _ in range(M)]
    time = T
    now = 0
    for i in range(N-1):
        time -= A[i]
        if time <= 0:
            print("No")
            return
        for j in range(M):
            if XY[j][0] == i+1:
                time += XY[j][1]
                break
    print("Yes")
