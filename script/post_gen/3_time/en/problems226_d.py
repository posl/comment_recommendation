Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

=======
Suggestion 2

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

=======
Suggestion 3

def main():
    N = int(input())
    x = []
    y = []
    for i in range(N):
        x_i, y_i = map(int, input().split())
        x.append(x_i)
        y.append(y_i)
    ans = 0
    for i in range(N):
        for j in range(i+1, N):
            ans = max(ans, abs(x[i]-x[j]) + abs(y[i]-y[j]))
    print(ans)

=======
Suggestion 4

def gcd(a, b):
    if a < b:
        return gcd(b, a)
    if b == 0:
        return a
    return gcd(b, a % b)

=======
Suggestion 5

def gcd(a,b):
    if a == 0:
        return b
    if b == 0:
        return a
    if a >= b:
        return gcd(a%b,b)
    if a < b:
        return gcd(a,b%a)

=======
Suggestion 6

def main():
    N = int(input())
    XY = [tuple(map(int, input().split())) for _ in range(N)]

    # (x, y) -> (x + a, y + b) となる a, b を全通り試す
    # その組み合わせを全て試してみる
    # その組み合わせの中で、全ての点を結ぶことができるか確認する
    # できるなら、その組み合わせの長さを記録する
    # できないなら、その組み合わせは捨てる
    # 最後に、残った組み合わせの中で最短のものを探す

    # (x, y) -> (x + a, y + b) となる a, b を全通り試す
    # その組み合わせを全て試してみる
    # その組み合わせの中で、全ての点を結ぶことができるか確認する
    # できるなら、その組み合わせの長さを記録する
    # できないなら、その組み合わせは捨てる
    # 最後に、残った組み合わせの中で最短のものを探す

    # (x, y) -> (x + a, y + b) となる a, b を全通り試す
    # その組み合わせを全て試してみる
    # その組み合わせの中で、全ての点を結ぶことができるか確認する
    # できるなら、その組み合わせの長さを記録する
    # できないなら、その組み合わせは捨てる
    # 最後

=======
Suggestion 7

def main():
    N = int(input())
    xy = []
    for _ in range(N):
        xy.append(list(map(int, input().split())))
    #print(xy)
    xy.sort()
    #print(xy)
    #print(xy[0][0])
    #print(xy[1][0])
    #print(xy[2][0])
    #print(xy[3][0])
    #print(xy[0][1])
    #print(xy[1][1])
    #print(xy[2][1])
    #print(xy[3][1])
    #print(xy[0][0] + xy[1][0] + xy[2][0] + xy[3][0])
    #print(xy[0][1] + xy[1][1] + xy[2][1] + xy[3][1])
    #print(xy[0][0] + xy[1][0] + xy[2][0] + xy[3][0] + xy[0][1] + xy[1][1] + xy[2][1] + xy[3][1])
    #print(xy[0][0] + xy[1][0] + xy[2][0] + xy[3][0] + xy[0][1] + xy[1][1] + xy[2][1] + xy[3][1] + xy[0][0] + xy[1][0] + xy[2][0] + xy[3][0] + xy[0][1] + xy[1][1] + xy[2][1] + xy[3][1])
    #print(xy[0][0] + xy[1][0] + xy[2][0] + xy[3][0] + xy[0][1] + xy[1][1] + xy[2][1] + xy[3][1] + xy[0][0] + xy[1][0] + xy[2][0] + xy[3][0] + xy[0][1] + xy[1][1] + xy[2][1] + xy[3][1] + xy[0][0] + xy[1][0] + xy[2][0] + xy[3][0] + xy[0][1] + xy[

=======
Suggestion 8

def get_abs(x, y):
    return abs(x) + abs(y)
