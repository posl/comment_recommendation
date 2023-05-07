def main():
    N, M, T = map(int, input().split())
    cafe = [list(map(int, input().split())) for _ in range(M)]
    battery = N
    for i in range(M):
        if i == 0:
            battery -= cafe[i][0]
        else:
            battery -= (cafe[i][0] - cafe[i-1][1])
        if battery <= 0:
            print("No")
            return
        battery += (cafe[i][1] - cafe[i][0])
        if battery > N:
            battery = N
    battery -= (T - cafe[M-1][1])
    if battery <= 0:
        print("No")
        return
    print("Yes")
