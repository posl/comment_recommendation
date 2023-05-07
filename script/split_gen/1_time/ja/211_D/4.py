def main():
    N, M = map(int, input().split())
    if M == 0:
        print(0)
        return
    AB = [list(map(int, input().split())) for _ in range(M)]
    AB = sorted(AB, key=lambda x: x[1])
    #print(AB)
    cnt = 1
    prev = AB[0][1]
    for i in range(1, M):
        if AB[i][0] < prev:
            continue
        cnt += 1
        prev = AB[i][1]
    print(cnt)
