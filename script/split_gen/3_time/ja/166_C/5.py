def main():
    N, M = map(int, input().split())
    H = list(map(int, input().split()))
    AB = []
    for i in range(M):
        AB.append(list(map(int, input().split())))
    count = 0
    for i in range(N):
        for j in range(M):
            if AB[j][0]-1 == i:
                if H[i] <= H[AB[j][1]-1]:
                    break
            elif AB[j][1]-1 == i:
                if H[i] <= H[AB[j][0]-1]:
                    break
        else:
            count += 1
    print(count)
