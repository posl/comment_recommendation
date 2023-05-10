Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    # input
    X, Y, Z, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))

    # compute
    AB = []
    for a in A:
        for b in B:
            AB.append(a + b)
    AB.sort(reverse=True)
    ABC = []
    for i in range(min(K, len(AB))):
        for c in C:
            ABC.append(AB[i] + c)
    ABC.sort(reverse=True)

    # output
    for i in range(K):
        print(ABC[i])

=======
Suggestion 2

def main():
    X,Y,Z,K = map(int,input().split())
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    C = list(map(int,input().split()))

    AB = []
    for a in A:
        for b in B:
            AB.append(a+b)
    AB.sort(reverse=True)
    AB = AB[:K]

    ABC = []
    for ab in AB:
        for c in C:
            ABC.append(ab+c)
    ABC.sort(reverse=True)
    ABC = ABC[:K]

    for abc in ABC:
        print(abc)

=======
Suggestion 3

def main():
    x,y,z,k = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    c = list(map(int,input().split()))

    ab = [i+j for i in a for j in b]
    ab.sort(reverse=True)
    ab = ab[:k]
    abc = [i+j for i in ab for j in c]
    abc.sort(reverse=True)
    abc = abc[:k]
    for i in abc:
        print(i)

=======
Suggestion 4

def main():
    x, y, z, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))

    ab = [i + j for i in a for j in b]
    ab.sort(reverse=True)

    abc = [i + j for i in ab[:k] for j in c]
    abc.sort(reverse=True)

    for i in range(k):
        print(abc[i])

=======
Suggestion 5

def main():
    # 標準入力を取得
    x, y, z, k = map(int, input().split())
    a_list = list(map(int, input().split()))
    b_list = list(map(int, input().split()))
    c_list = list(map(int, input().split()))
    #print(x, y, z, k)
    #print(a_list)
    #print(b_list)
    #print(c_list)

    # 3つのケーキの選び方は X × Y × Z 通りあり、それらをケーキの美味しさの合計が大きい順に並べると以下の通りです。
    # (A_2, B_2, C_2): 6 + 5 + 8 = 19
    # (A_1, B_2, C_2): 4 + 5 + 8 = 17
    # (A_2, B_1, C_2): 6 + 1 + 8 = 15
    # (A_2, B_2, C_1): 6 + 5 + 3 = 14
    # (A_1, B_1, C_2): 4 + 1 + 8 = 13
    # (A_1, B_2, C_1): 4 + 5 + 3 = 12
    # (A_2, B_1, C_1): 6 + 1 + 3 = 10
    # (A_1, B_1, C_1): 4 + 1 + 3 = 8

    # 3つのケーキの選び方は X × Y × Z 通りあり、それらをケーキの美味しさの合計が大きい順に並べると以下の通りです。
    # (A_2, B_2, C_2): 6 + 5 + 8 = 19
    # (A_1, B_2, C_2): 4 + 5 + 8 = 17
    # (A_2, B_1

=======
Suggestion 6

def main():
    pass

=======
Suggestion 7

def main():
    x,y,z,k = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    c = list(map(int,input().split()))

    ab = [a[i]+b[j] for i in range(x) for j in range(y)]
    ab.sort(reverse=True)
    abc = [ab[i]+c[j] for i in range(k) for j in range(z)]
    abc.sort(reverse=True)
    for i in range(k):
        print(abc[i])

=======
Suggestion 8

def main():
    x,y,z,k = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    c = list(map(int,input().split()))
    ab = []
    for i in range(x):
        for j in range(y):
            ab.append(a[i]+b[j])
    ab.sort(reverse=True)
    ab = ab[:k]
    abc = []
    for i in range(len(ab)):
        for j in range(z):
            abc.append(ab[i]+c[j])
    abc.sort(reverse=True)
    for i in range(k):
        print(abc[i])

=======
Suggestion 9

def main():
    x,y,z,k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))

    a.sort(reverse=True)
    b.sort(reverse=True)
    c.sort(reverse=True)

    ab = []
    for i in range(x):
        for j in range(y):
            ab.append(a[i]+b[j])

    ab.sort(reverse=True)

    abc = []
    for i in range(min(k, x*y)):
        for j in range(z):
            abc.append(ab[i]+c[j])

    abc.sort(reverse=True)

    for i in range(k):
        print(abc[i])

=======
Suggestion 10

def main():
    x, y, z, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))

    ab = []
    for i in range(x):
        for j in range(y):
            ab.append(a[i] + b[j])
    ab.sort(reverse=True)

    abc = []
    for i in range(min(k, x * y)):
        for j in range(z):
            abc.append(ab[i] + c[j])
    abc.sort(reverse=True)

    for i in range(k):
        print(abc[i])
