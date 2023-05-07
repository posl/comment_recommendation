def main():
    N, X = map(int, input().split())
    alcohols = []
    for i in range(N):
        alcohols.append(list(map(int, input().split())))
    alcohol = 0
    for i in range(N):
        alcohol += alcohols[i][0] * alcohols[i][1] * 0.01
        if alcohol > X:
            print(i + 1)
            break
    else:
        print(-1)
