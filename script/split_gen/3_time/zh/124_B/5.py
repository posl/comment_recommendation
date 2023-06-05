def main():
    N = int(input())
    H = list(map(int, input().split()))
    cnt = 0
    max_h = 0
    for i in range(N):
        if max_h <= H[i]:
            cnt += 1
            max_h = H[i]
    print(cnt)
