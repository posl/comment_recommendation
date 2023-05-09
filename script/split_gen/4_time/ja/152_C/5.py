def main():
    N = int(input())
    P = list(map(int, input().split()))
    cnt = 0
    min = N+1
    for i in range(N):
        if min > P[i]:
            cnt += 1
            min = P[i]
    print(cnt)
