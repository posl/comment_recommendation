def main():
    N, M = map(int, input().split())
    if M == 0:
        print(3**N)
        return
    ab = [list(map(int, input().split())) for _ in range(M)]
    ab = sorted(ab, key=lambda x: x[0])
    ab = sorted(ab, key=lambda x: x[1])
    ans = 1
    for i in range(M):
        if i == 0:
            ans *= 3
            continue
        if ab[i-1][1] == ab[i][1]:
            if ab[i-1][0] == ab[i][0]:
                ans *= 1
            else:
                ans *= 2
        else:
            ans *= 3
    print(ans)
