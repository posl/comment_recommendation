def main():
    N = int(input())
    ladders = [list(map(int, input().split())) for _ in range(N)]
    ladders.sort(key=lambda x: x[1])
    now = 0
    for i in range(N):
        if ladders[i][0] > now:
            now = ladders[i][0]
        else:
            now = ladders[i][1]
    print(now)
