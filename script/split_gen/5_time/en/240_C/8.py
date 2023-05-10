def main():
    N, X = map(int, input().split())
    AB = [list(map(int, input().split())) for i in range(N)]
    distance = 0
    for i in range(N):
        distance += AB[i][0] * AB[i][1]
        if distance > X * 100:
            print("No")
            return
    print("Yes")
