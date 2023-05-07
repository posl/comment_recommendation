def main():
    n = int(input())
    h = list(map(int, input().split()))
    cnt = 0
    max_cnt = 0
    for i in range(1, n):
        if h[i-1] >= h[i]:
            cnt += 1
        else:
            cnt = 0
        max_cnt = max(max_cnt, cnt)
    print(max_cnt)
