def main():
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(M)]
    AB.sort(key=lambda x: x[1])
    #print(AB)
    cnt = 0
    i = 0
    while i < M:
        cnt += 1
        j = i
        while j < M and AB[j][0] <= AB[i][1]:
            j += 1
        i = j
    print(cnt)
