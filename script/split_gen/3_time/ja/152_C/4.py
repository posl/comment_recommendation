def main():
    N = int(input())
    P = list(map(int, input().split()))
    min_num = P[0]
    cnt = 0
    for i in range(N):
        if min_num >= P[i]:
            cnt += 1
            min_num = P[i]
    print(cnt)
