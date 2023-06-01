Synthesizing 10/10 solutions

=======
Suggestion 1

def solution():
    n, k = map(int, input().split())
    ab = [tuple(map(int, input().split())) for _ in range(n)]
    ab.sort(key=lambda x: x[0])

    for a, b in ab:
        if a > k:
            break
        k += b
    print(k)

=======
Suggestion 2

def main():
    N,K = map(int,input().split())
    AB = [map(int,input().split()) for _ in range(N)]
    A,B = [list(i) for i in zip(*AB)]
    A.append(10**100)
    B.append(0)
    from bisect import bisect_left
    index = bisect_left(A,K)
    print(B[index-1])

=======
Suggestion 3

def main():
    # 读入数据
    n, k = map(int, input().split())
    ab = [list(map(int, input().split())) for _ in range(n)]
    # 按照村庄的位置排序
    ab.sort(key=lambda x: x[0])
    # 遍历村庄
    i = 0
    while k > 0 and i < n:
        # k - ab[i][0]是从当前村庄到下一个村庄所需的日元数
        # k - ab[i][0] < 0意味着无法到达下一个村庄
        if k - ab[i][0] < 0:
            break
        # 否则可以到达下一个村庄
        k += ab[i][1] - ab[i][0]
        i += 1
    # 输出结果
    print(k + ab[i - 1][0] if i > 0 else k)

=======
Suggestion 4

def main():
    n,k = map(int,input().split())
    ab = []
    for i in range(n):
        a,b = map(int,input().split())
        ab.append([a,b])
    ab.sort(key=lambda x:x[0])
    now = 0
    for i in range(n):
        if ab[i][0] > now + k:
            break
        k += ab[i][1]
        now = ab[i][0]
    print(now+k)

=======
Suggestion 5

def main():
    n, k = map(int, input().split())
    friends = []
    for i in range(n):
        a, b = map(int, input().split())
        friends.append((a, b))
    friends.sort()
    friends.append((10**100, 0))
    money = k
    pos = 0
    for i in range(n):
        money += friends[i][1]
        if money >= friends[i+1][0]:
            money -= friends[i+1][0]
            pos = friends[i+1][0]
        else:
            pos += money
            break
    print(pos)

=======
Suggestion 6

def main():
    n, k = map(int, input().split())
    friends = []
    for i in range(n):
        friends.append(list(map(int, input().split())))

    friends = sorted(friends, key=lambda x: x[0])
    # print(friends)
    money = k
    village = 0
    for i in range(n):
        if money >= friends[i][0] - village:
            money += friends[i][1]
            village = friends[i][0]
        else:
            break
    print(village + money)

=======
Suggestion 7

def solve():
    n, k = map(int, input().split())
    AB = []
    for _ in range(n):
        a, b = map(int, input().split())
        AB.append((a, b))
    AB.sort()
    now = 0
    for a, b in AB:
        if a - now > k:
            break
        k += b - (a - now)
        now = a
    print(now + k)


solve()

=======
Suggestion 8

def main():
    n, k = map(int, input().split())
    ab = [list(map(int, input().split())) for _ in range(n)]
    ab.sort()
    for a, b in ab:
        if k < a:
            break
        k += b
    print(k)

=======
Suggestion 9

def main():
    N, K = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(N)]
    AB.sort(key=lambda x: x[0])

    money = K
    for a, b in AB:
        if a <= money:
            money += b
        else:
            break
    print(money)

=======
Suggestion 10

def main():
    n,k = map(int,input().split())
    money = 0
    for i in range(n):
        a,b = map(int,input().split())
        if k >= a - money:
            k = k - (a - money) + b
            money = a
        else:
            print(money + k)
            exit()
    print(money + k)
