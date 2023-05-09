def main():
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(M)]
    AB.sort(key=lambda x: x[1])
    cnt = 0
    for i in range(M):
        if cnt == 0:
            cnt += 1
            continue
        if AB[i][0] < AB[i-1][1] and AB[i][1] > AB[i-1][1]:
            cnt += 1
    if cnt == M:
        print("Yes")
    else:
        print("No")
