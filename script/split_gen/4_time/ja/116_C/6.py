def main():
    N = int(input())
    h = list(map(int,input().split()))
    cnt = 0
    while sum(h) > 0:
        for i in range(N):
            if h[i] > 0:
                cnt += 1
                h[i] -= 1
        # print(h)
    print(cnt)
