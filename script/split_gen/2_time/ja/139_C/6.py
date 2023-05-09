def main():
    N = int(input())
    H = list(map(int, input().split()))
    cnt = 0
    tmp = 0
    for i in range(1, N):
        if H[i-1] >= H[i]:
            tmp += 1
        else:
            tmp = 0
        cnt = max(cnt, tmp)
    print(cnt)
