def main():
    N, X = map(int, input().split())
    jumps = [list(map(int, input().split())) for _ in range(N)]
    distance = 0
    for i in range(N):
        distance += jumps[i][0]
        if distance > X:
            print("No")
            return
        distance += jumps[i][1]
    if distance > X:
        print("No")
    else:
        print("Yes")
