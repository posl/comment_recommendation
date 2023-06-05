def main():
    N = int(input())
    H = list(map(int, input().split()))
    cnt = 0
    max_cnt = 0
    for i in range(1, N):
        if H[i-1] >= H[i]:
            cnt += 1
            max_cnt = max(max_cnt, cnt)
        else:
            cnt = 0
    print(max_cnt)
