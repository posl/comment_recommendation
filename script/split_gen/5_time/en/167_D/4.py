def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    ans = 0
    cnt = 0
    while True:
        ans = A[ans] - 1
        cnt += 1
        if cnt == K:
            print(ans + 1)
            break
        if ans == 0:
            print(ans + 1)
            break
