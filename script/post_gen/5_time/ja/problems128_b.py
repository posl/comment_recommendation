Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    sp = []
    for i in range(n):
        s, p = input().split()
        sp.append([s, int(p)])
    sp = sorted(sp, key=lambda x: x[1], reverse=True)
    sp = sorted(sp, key=lambda x: x[0])
    for i in range(n):
        print(sp[i][2])

=======
Suggestion 2

def main():
    n = int(input())
    s = []
    p = []
    for i in range(n):
        s_i, p_i = input().split()
        s.append(s_i)
        p.append(int(p_i))
    restaurant = []
    for i in range(n):
        restaurant.append([s[i], p[i], i+1])
    restaurant.sort(key=lambda x: x[1], reverse=True)
    restaurant.sort(key=lambda x: x[0])
    for i in range(n):
        print(restaurant[i][2])

=======
Suggestion 3

def main():
    N = int(input())
    S = []
    P = []
    for i in range(N):
        s, p = input().split()
        S.append(s)
        P.append(int(p))
    #print(S)
    #print(P)
    #辞書順でソート
    SP = sorted(zip(S, P), key=lambda x: x[0])
    #print(SP)
    #辞書順でソートしたリストを点数降順でソート
    SPP = sorted(SP, key=lambda x: x[1], reverse=True)
    #print(SPP)
    #点数降順でソートしたリストを辞書順でソート
    SPPP = sorted(SPP, key=lambda x: x[0])
    #print(SPPP)
    #リストの要素から点数だけを取り出して出力
    for i in range(N):
        print(SPPP[i][1])

=======
Suggestion 4

def main():
    n = int(input())
    restaurants = []
    for i in range(n):
        restaurant = input().split()
        restaurants.append([restaurant[0], int(restaurant[1]), i+1])
    restaurants = sorted(restaurants, key=lambda x: (x[0], -x[1]))
    for i in range(n):
        print(restaurants[i][2])

=======
Suggestion 5

def main():
    N = int(input())
    restaurants = []
    for i in range(N):
        S, P = input().split()
        restaurants.append((S, int(P), i + 1))
    restaurants.sort(key=lambda x: x[1], reverse=True)
    restaurants.sort(key=lambda x: x[0])
    for r in restaurants:
        print(r[2])

=======
Suggestion 6

def main():
    N = int(input())
    arr = []
    for i in range(N):
        s, p = input().split()
        arr.append((s, int(p), i+1))
    arr = sorted(arr, key=lambda x: (x[0], -x[1]))
    for i in range(N):
        print(arr[i][2])

=======
Suggestion 7

def main():
    n = int(input())
    restaurants = []
    for i in range(n):
        s, p = input().split()
        restaurants.append((s, int(p), i+1))
    restaurants.sort(key=lambda x: (x[0], -x[1]))
    for i in range(n):
        print(restaurants[i][2])

=======
Suggestion 8

def main():
    N = int(input())
    restaurants = []
    for i in range(N):
        S, P = input().split()
        restaurants.append((S, int(P), i + 1))
    restaurants.sort(key=lambda x: (x[0], -x[1]))
    for _, _, i in restaurants:
        print(i)

=======
Suggestion 9

def main():
    n = int(input())
    restaurants = []
    for i in range(n):
        s, p = input().split()
        restaurants.append((s, int(p), i+1))
    restaurants.sort(key=lambda x: (x[0], -x[1]))
    for r in restaurants:
        print(r[2])

=======
Suggestion 10

def main():
    N = int(input())
    S = []
    P = []
    for i in range(N):
        s, p = input().split()
        S.append(s)
        P.append(int(p))
    #print(S)
    #print(P)
    dic = {}
    for i in range(N):
        if S[i] in dic:
            dic[S[i]].append([P[i], i+1])
        else:
            dic[S[i]] = [[P[i], i+1]]
    #print(dic)
    for i in dic:
        dic[i].sort(reverse=True)
    #print(dic)
    S.sort()
    #print(S)
    for i in S:
        for j in range(len(dic[i])):
            print(dic[i][j][1])
