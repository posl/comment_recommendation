def main():
    N = int(input())
    H = list(map(int, input().split()))
    cnt = 1
    for i in range(1, N):
        if max(H[:i]) <= H[i]:
            cnt += 1
    print(cnt)
