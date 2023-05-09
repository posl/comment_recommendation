def main():
    N = int(input())
    P = list(map(int, input().split()))
    cnt = 1
    min = P[0]
    for i in range(1, N):
        if min >= P[i]:
            cnt += 1
            min = P[i]
    print(cnt)
