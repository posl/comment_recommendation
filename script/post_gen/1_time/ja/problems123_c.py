Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N = int(input())
    A = int(input())
    B = int(input())
    C = int(input())
    D = int(input())
    E = int(input())

    print(5 + (N - 1) // min(A, B, C, D, E))

=======
Suggestion 2

def main():
    n = int(input())
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    e = int(input())
    m = min(a,b,c,d,e)
    print(5 + (n-1)//m)

=======
Suggestion 3

def main():
    N = int(input())
    A = int(input())
    B = int(input())
    C = int(input())
    D = int(input())
    E = int(input())
    #print(N,A,B,C,D,E)
    #print("N:{}".format(N))
    #print("A:{}".format(A))
    #print("B:{}".format(B))
    #print("C:{}".format(C))
    #print("D:{}".format(D))
    #print("E:{}".format(E))
    #print("N:{}".format(N))
    #print("A:{}".format(A))
    #print("B:{}".format(B))
    #print("C:{}".format(C))
    #print("D:{}".format(D))
    #print("E:{}".format(E))
    #print("N:{}".format(N))
    #print("A:{}".format(A))
    #print("B:{}".format(B))
    #print("C:{}".format(C))
    #print("D:{}".format(D))
    #print("E:{}".format(E))
    #print("N:{}".format(N))
    #print("A:{}".format(A))
    #print("B:{}".format(B))
    #print("C:{}".format(C))
    #print("D:{}".format(D))
    #print("E:{}".format(E))
    #print("N:{}".format(N))
    #print("A:{}".format(A))
    #print("B:{}".format(B))
    #print("C:{}".format(C))
    #print("D:{}".format(D))
    #print("E:{}".format(E))
    #print("N:{}".format(N))
    #print("A:{}".format(A))
    #print("B:{}".format(B))
    #print("C:{}".format(C))
    #print("D:{}".format(D))
    #print("E:{}".format(E))
    #print("N:{}".format(N))
    #print("A:{}".format(A))
    #print("B:{}".format(B))
    #print("C:{}".format(C))
    #print("D:{}".format(D))
    #print("E:{}".format(E))
    #print("N:{}".format(N))
    #print("A:{}".format(A))
    #print("B:{}".format(B))
    #

=======
Suggestion 4

def main():
    N = int(input())
    A = int(input())
    B = int(input())
    C = int(input())
    D = int(input())
    E = int(input())

    if N % A == 0:
        train = int(N / A)
    else:
        train = int(N / A) + 1
    if N % B == 0:
        bus = int(N / B)
    else:
        bus = int(N / B) + 1
    if N % C == 0:
        taxi = int(N / C)
    else:
        taxi = int(N / C) + 1
    if N % D == 0:
        plane = int(N / D)
    else:
        plane = int(N / D) + 1
    if N % E == 0:
        ship = int(N / E)
    else:
        ship = int(N / E) + 1

    a = max(train, bus, taxi, plane, ship)
    print(a + 4)

=======
Suggestion 5

def main():
    N = int(input())
    A = int(input())
    B = int(input())
    C = int(input())
    D = int(input())
    E = int(input())

    print(4 + (N + min([A,B,C,D,E])-1)//min([A,B,C,D,E]))

=======
Suggestion 6

def main():
    n = int(input())
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    e = int(input())
    min = 0
    for i in range(0, 5):
        if i == 0:
            min = min + 1
        elif i == 1:
            min = min + (n + a - 1) // a
        elif i == 2:
            min = min + (n + b - 1) // b
        elif i == 3:
            min = min + (n + c - 1) // c
        elif i == 4:
            min = min + (n + d - 1) // d
        else:
            min = min + (n + e - 1) // e
    print(min)

=======
Suggestion 7

def solve(n, a, b, c, d, e):
    m = min(a, b, c, d, e)
    if n <= m:
        return 5
    return 4 + (n + m - 1) // m

=======
Suggestion 8

def main():
    import sys
    from math import ceil
    readline = sys.stdin.buffer.readline
    mod = 10**9+7
    N = int(readline())
    A = int(readline())
    B = int(readline())
    C = int(readline())
    D = int(readline())
    E = int(readline())
    print(ceil(N/min(A,B,C,D,E))+4)

=======
Suggestion 9

def main():
    n = int(input())
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    e = int(input())

    # 交通機関の数は5つ
    # 交通機関の移動時間は1分
    # 交通機関の乗車人数はそれぞれA,B,C,D,E
    # 乗車人数が多い順に乗車していく
    # 乗車人数が多い順に乗車していくと、乗車人数が多い交通機関で移動する時間が短くなる
    # 乗車人数が多い順に乗車していくと、乗車人数が多い交通機関で移動する時間が短くなるので、乗車人数が多い順に乗車していく
    # 乗車人数が多い順に乗車していくと、乗車人数が多い交通機関で移動する時間が短くなるので、乗車人数が多い順に乗車していく
    # 乗車人数が多い順に乗車していくと、乗車人数が多い交通機関で移動する時間が短くなるので、乗車人数が多い順に乗車していく
    # 乗車人数が多い順に乗車していくと、乗車人数が多い交通機関で移動する時間が短くなるので、乗車人数が多い順に乗車していく
    # 乗
