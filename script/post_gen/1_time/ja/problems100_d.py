Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, M = map(int, input().split())
    cake = []
    for i in range(N):
        cake.append(list(map(int, input().split())))
    ans = 0
    for i in range(8):
        cake.sort(key=lambda x: -abs(x[i%3]) if i < 3 else abs(x[i%3]))
        ans = max(ans, sum([abs(sum(cake[j][i%3] for j in range(M))) for i in range(3)]))
    print(ans)

=======
Suggestion 2

def main():
    n, m = map(int, input().split())
    cake = []
    for i in range(n):
        cake.append(list(map(int, input().split())))
    ans = 0
    for i in range(8):
        cake.sort(key = lambda x: sum([(-1)**((i>>j)&1)*x[j] for j in range(3)]), reverse = True)
        ans = max(ans, sum([sum([(-1)**((i>>j)&1)*cake[k][j] for j in range(3)]) for k in range(m)]))
    print(ans)

=======
Suggestion 3

def main():
    N, M = map(int, input().split())
    cake = []
    for _ in range(N):
        cake.append(list(map(int, input().split())))
    ans = 0
    for i in range(8):
        tmp = []
        for j in range(N):
            tmp.append(sum([cake[j][k] * (-1)**(i>>k & 1) for k in range(3)]))
        tmp.sort(reverse=True)
        ans = max(ans, sum(tmp[:M]))
    print(ans)

=======
Suggestion 4

def main():
    N, M = map(int, input().split())
    cake = [list(map(int, input().split())) for _ in range(N)]
    
    ans = 0
    for i in range(2**3):
        tmp = []
        for j in range(N):
            tmp.append(sum([cake[j][k] * (-1)**((i>>k)&1) for k in range(3)]))
        tmp.sort(reverse=True)
        ans = max(ans, sum(tmp[:M]))
    
    print(ans)

=======
Suggestion 5

def main():
    n, m = map(int, input().split())
    cake = []
    for _ in range(n):
        cake.append(list(map(int, input().split())))
    ans = 0
    for i in range(2**3):
        tmp = []
        for j in range(n):
            tmp.append(sum([cake[j][k] if (i >> k) & 1 else -cake[j][k] for k in range(3)]))
        tmp.sort(reverse=True)
        ans = max(ans, sum(tmp[:m]))
    print(ans)

=======
Suggestion 6

def main():
    N, M = map(int, input().split())
    cake = [list(map(int, input().split())) for _ in range(N)]
    ans = 0
    for i in range(2**3):
        tmp = [0] * N
        for j in range(N):
            for k in range(3):
                if i >> k & 1:
                    tmp[j] += cake[j][k]
                else:
                    tmp[j] -= cake[j][k]
        tmp.sort(reverse=True)
        ans = max(ans, sum(tmp[:M]))
    print(ans)

=======
Suggestion 7

def main():
    n, m = map(int, input().split())
    cake = [list(map(int, input().split())) for _ in range(n)]
    ans = 0
    for i in range(8):
        cake.sort(key=lambda x: x[i%3]*(-1)**(i//3))
        ans = max(ans, sum(map(abs, [sum(x) for x in zip(*cake[:m])])))
    print(ans)

=======
Suggestion 8

def main():
    N, M = map(int, input().split())
    cake = [list(map(int, input().split())) for _ in range(N)]
    ans = -float("inf")
    for i in range(2**3):
        tmp = 0
        for j in range(N):
            tmp += max([cake[j][k] if (i >> k) & 1 else -cake[j][k] for k in range(3)])
        ans = max(ans, tmp)
    print(ans)

=======
Suggestion 9

def main():
    n, m = map(int, input().split())
    cake = []
    for i in range(n):
        cake.append(list(map(int, input().split())))
    #print(cake)
    
    ans = 0
    for i in range(2**3):
        tmp = []
        for j in range(n):
            tmp.append(cake[j][0] * ((i >> 0) & 1) + cake[j][1] * ((i >> 1) & 1) + cake[j][2] * ((i >> 2) & 1))
        tmp.sort(reverse=True)
        ans = max(ans, sum(tmp[:m]))
    print(ans)

=======
Suggestion 10

def main():
    N, M = map(int, input().split())
    # この問題では、綺麗さ、おいしさ、人気度の順にソートすると、
    # 綺麗さは降順、おいしさは昇順、人気度は降順になる。
    # したがって、綺麗さの最大値は、最大の M 個の綺麗さの合計となる。
    # おいしさの最大値は、最小の M 個のおいしさの合計となる。
    # 人気度の最大値は、最大の M 個の人気度の合計となる。
    # したがって、綺麗さ、おいしさ、人気度の合計の最大値は、
    # max(綺麗さの合計) + min(おいしさの合計) + max(人気度の合計) となる。
    # これを全ての組み合わせについて計算すると、計算量が O(N^3) となってしまう。
    # しかし、綺麗さ、おいしさ、人気度の順にソートしたとき、
    # それぞれの要素を固定して、残りの要素の合計を計算することで、
    # それぞれの合計の最大値を O(N^2) で求めることができる。
    # したがって、全体の計算量は O(N^2) となる。
    # また、綺麗さ、おいしさ、人気度の順にソートすると、
    # 綺麗さは降順、おいしさは昇順、人気度は降順にな
