def main():
    N = int(input())
    P = list(map(int, input().split()))
    min = 0
    cnt = 0
    for i in range(N):
        if P[i] >= min:
            cnt += 1
            min = P[i]
    print(cnt)
