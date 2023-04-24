Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, M = map(int, input().split())
    cakes = []
    for _ in range(N):
        x, y, z = map(int, input().split())
        cakes.append((x, y, z))
    ans = 0
    for i in range(2**3):
        cakes.sort(key=lambda x: (-1)**(i & 1) * x[(i & 2) >> 1] + (-1)**(i & 4) * x[(i & 8) >> 3] + (-1)**(i & 16) * x[(i & 32) >> 5], reverse=True)
        ans = max(ans, sum(cakes[j][0] + cakes[j][1] + cakes[j][2] for j in range(M)))
    print(ans)

main()

=======
Suggestion 2

def main():
    N, M = map(int, input().split())
    cakes = []
    for _ in range(N):
        cakes.append(list(map(int, input().split())))
    ans = 0
    for i in range(8):
        tmp = [0] * N
        for j in range(N):
            for k in range(3):
                if i & (1 << k):
                    tmp[j] += cakes[j][k]
                else:
                    tmp[j] -= cakes[j][k]
        tmp.sort(reverse=True)
        ans = max(ans, sum(tmp[:M]))
    print(ans)

=======
Suggestion 3

def main():
    N, M = map(int, input().split())
    cake = [list(map(int, input().split())) for _ in range(N)]
    ans = 0
    for i in range(2 ** 3):
        tmp = [0] * N
        for j in range(N):
            for k in range(3):
                if (i >> k) & 1:
                    tmp[j] += cake[j][k]
                else:
                    tmp[j] -= cake[j][k]
        tmp.sort(reverse=True)
        ans = max(ans, sum(tmp[:M]))
    print(ans)

=======
Suggestion 4

def main():
    N, M = map(int, input().split())
    cakes = [list(map(int, input().split())) for _ in range(N)]
    ans = 0
    for i in range(8):
        tmp = []
        for j in range(N):
            tmp.append(sum([(-1)**((i>>k)&1)*cakes[j][k] for k in range(3)]))
        tmp.sort(reverse=True)
        ans = max(ans, sum(tmp[:M]))
    print(ans)

=======
Suggestion 5

def main():
    N, M = list(map(int, input().split()))
    cake = []
    for i in range(N):
        cake.append(list(map(int, input().split())))
    ans = 0
    for i in range(8):
        tmp = []
        for j in range(N):
            tmp.append(sum([cake[j][k] if i&(1<<k) else -cake[j][k] for k in range(3)]))
        tmp.sort(reverse=True)
        ans = max(ans, sum(tmp[:M]))
    print(ans)

=======
Suggestion 6

def main():
    N, M = map(int, input().split())
    cakes = [list(map(int, input().split())) for _ in range(N)]
    ans = 0
    for i in range(8):
        cakes.sort(reverse=True, key=lambda x: x[0] if i & 1 else -x[0])
        cakes.sort(reverse=True, key=lambda x: x[1] if i & 2 else -x[1])
        cakes.sort(reverse=True, key=lambda x: x[2] if i & 4 else -x[2])
        ans = max(ans, sum(map(abs, [sum(cake) for cake in zip(*cakes[:M])])))
    print(ans)

=======
Suggestion 7

def main():
    N, M = map(int, input().split())
    cake = [list(map(int, input().split())) for _ in range(N)]
    ans = 0
    for i in range(1, 2**3):
        tmp = 0
        for j in range(N):
            tmp += sum([cake[j][k] if (i >> k) & 1 else -cake[j][k] for k in range(3)])
        ans = max(ans, tmp)
    print(ans)

=======
Suggestion 8

def main():
    import sys
    from itertools import combinations
    input = sys.stdin.readline
    N, M = map(int, input().split())
    xyz = [list(map(int, input().split())) for _ in range(N)]
    ans = -10**18
    for i in range(2**3):
        tmp = []
        for j in range(N):
            tmp.append(sum([(-1)**((i>>k)&1)*xyz[j][k] for k in range(3)]))
        tmp.sort(reverse=True)
        ans = max(ans, sum(tmp[:M]))
    print(ans)

=======
Suggestion 9

def main():
    N, M = map(int, input().split())
    cakes = [tuple(map(int, input().split())) for _ in range(N)]
    ans = 0
    for i in range(2**3):
        sign = [1 if i >> j & 1 else -1 for j in range(3)]
        cakes.sort(key=lambda x: sum(sign[j]*x[j] for j in range(3)), reverse=True)
        ans = max(ans, sum(sum(sign[j]*x[j] for j in range(3)) for x in cakes[:M]))
    print(ans)

=======
Suggestion 10

def main():
    N, M = map(int, input().split())
    # N: number of cakes
    # M: number of cakes to have

    # x_i, y_i, z_i (1 <= i <= N) are integers between -10^18 and 10^18 (inclusive)
    # x_i, y_i, z_i (1 <= i <= N) are the beauty, tastiness, popularity of the i-th kind of cake
    cakes = []
    for i in range(N):
        x, y, z = map(int, input().split())
        cakes.append((x, y, z))

    # The total beauty, tastiness and popularity will be as follows:
    # Beauty: sum of the beauty of the cakes
    # Tastiness: sum of the tastiness of the cakes
    # Popularity: sum of the popularity of the cakes
    # The value (the absolute value of the total beauty) + (the absolute value of the total tastiness) + (the absolute value of the total popularity) here is 13 + 17 + 26 = 56. This is the maximum value.
    # The value (the absolute value of the total beauty) + (the absolute value of the total tastiness) + (the absolute value of the total popularity) here is 21 + 24 + 9 = 54. This is the maximum value.
    # The value (the absolute value of the total beauty) + (the absolute value of the total tastiness) + (the absolute value of the total popularity) here is 323 + 66 + 249 = 638. This is the maximum value.
    # The value (the absolute value of the total beauty) + (the absolute value of the total tastiness) + (the absolute value of the total popularity) here is 30000000000. This is the maximum value.
    # The value (the absolute value of the total beauty) + (the absolute value of the total tastiness) + (the absolute value of the total popularity) here is 30000000000. This is the maximum value.
    # The value (the absolute value of the total beauty) + (the absolute value of the total tastiness) + (the absolute value of the total popularity) here is 30000000000. This is the maximum value.
    # The value (the absolute
