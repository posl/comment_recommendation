def main():
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(M)]
    K = int(input())
    CD = [list(map(int, input().split())) for _ in range(K)]
    res = 0
    for i in range(2 ** K):
        balls = [0] * (N + 1)
        for j in range(K):
            if (i >> j) & 1:
                balls[CD[j][0]] += 1
            else:
                balls[CD[j][1]] += 1
        tmp = 0
        for a, b in AB:
            if balls[a] > 0 and balls[b] > 0:
                tmp += 1
        res = max(res, tmp)
    print(res)

if __name__ == '__main__':
    main()