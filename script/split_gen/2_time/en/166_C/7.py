def main():
    N, M = map(int, input().split())
    H = list(map(int, input().split()))
    AB = [list(map(int, input().split())) for _ in range(M)]
    result = 0
    for i in range(N):
        for j in range(M):
            if AB[j][0] == i+1 and H[i] <= H[AB[j][1]-1]:
                break
            if AB[j][1] == i+1 and H[i] <= H[AB[j][0]-1]:
                break
        else:
            result += 1
    print(result)
