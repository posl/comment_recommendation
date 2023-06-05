def main():
    n = int(input())
    h = list(map(int, input().split()))
    cnt = 0
    tmp = 0
    for i in range(1, n):
        if h[i-1] >= h[i]:
            tmp += 1
        else:
            tmp = 0
        if cnt < tmp:
            cnt = tmp
    print(cnt)
