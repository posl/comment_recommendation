Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def det(a, b, c, d):
    return a * d - b * c

a, b = map(int, input().split())
c, d = map(int, input().split())
print(det(a, b, c, d))

=======
Suggestion 2

def main():
    # 读取数据
    a, b = map(int, input().split())
    c, d = map(int, input().split())
    # 计算结果
    ans = a * d - b * c
    # 输出结果
    print(ans)

=======
Suggestion 3

def main():
    a, b = map(int, input().split())
    c, d = map(int, input().split())
    print(a*d-b*c)

=======
Suggestion 4

def main():
    a, b = [int(x) for x in input().split()]
    c, d = [int(x) for x in input().split()]
    print(a*d-b*c)

=======
Suggestion 5

def main():
    a,b,c,d = map(int, input().split())
    print(a*d-b*c)

=======
Suggestion 6

def main():
    a = []
    b = []
    for i in range(2):
        a.append(list(map(int, input().split())))
    for i in range(2):
        b.append(list(map(int, input().split())))
    print(a[0][0]*b[0][0]+a[0][1]*b[1][0], a[0][0]*b[0][1]+a[0][1]*b[1][1])
    print(a[1][0]*b[0][0]+a[1][1]*b[1][0], a[1][0]*b[0][1]+a[1][1]*b[1][1])
