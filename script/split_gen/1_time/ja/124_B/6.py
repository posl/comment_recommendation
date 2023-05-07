def main():
    N = int(input())
    H = list(map(int, input().split()))
    cnt = 0
    for i in range(N):
        if i == 0:
            cnt += 1
        else:
            if max(H[:i]) <= H[i]:
                cnt += 1
    print(cnt)
