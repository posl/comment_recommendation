Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N = int(input())
    S = []
    P = []
    for i in range(N):
        s, p = input().split()
        S.append(s)
        P.append(int(p))
    for i in range(N):
        for j in range(N):
            if S[i] < S[j]:
                S[i], S[j] = S[j], S[i]
                P[i], P[j] = P[j], P[i]
            elif S[i] == S[j]:
                if P[i] > P[j]:
                    S[i], S[j] = S[j], S[i]
                    P[i], P[j] = P[j], P[i]
    for i in range(N):
        for j in range(N):
            if S[i] == S[j]:
                if P[i] == P[j]:
                    if i < j:
                        S[i], S[j] = S[j], S[i]
                        P[i], P[j] = P[j], P[i]
    for i in range(N):
        print(S.index(S[i])+1)

main()

=======
Suggestion 2

def main():
    n = int(input())
    data = []
    for i in range(n):
        s, p = input().split()
        data.append([s, int(p), i+1])
    data.sort(key=lambda x:(x[0],-x[1]))
    for i in range(n):
        print(data[i][2])

=======
Suggestion 3

def main():
    N = int(input())
    data = []
    for i in range(N):
        S, P = input().split()
        data.append([S, int(P), i+1])
    data.sort(key=lambda x: (x[0], -x[1]))
    for d in data:
        print(d[2])

=======
Suggestion 4

def main():
    N = int(input())
    data = []
    for i in range(N):
        s, p = input().split()
        data.append([s, int(p), i + 1])
    data.sort(key=lambda x: (x[0], -x[1]))
    for i in data:
        print(i[2])

=======
Suggestion 5

def main():
    N = int(input())
    restaurant = []
    for i in range(N):
        S, P = input().split()
        P = int(P)
        restaurant.append([i+1, S, P])
    restaurant.sort(key=lambda x: (x[1], -x[2]))
    for i in range(N):
        print(restaurant[i][0])

=======
Suggestion 6

def main():
    N = int(input())
    lst = []
    for i in range(N):
        S, P = input().split()
        lst.append([S, int(P), i+1])
    lst.sort(key=lambda x: (-x[1], x[0], x[2]))
    for i in range(N):
        print(lst[i][2])

=======
Suggestion 7

def main():
    N = int(input())
    # レストランのリスト
    restaurants = []
    for i in range(N):
        s, p = input().split()
        restaurants.append((s, int(p), i+1))
    # レストランのリストをソート
    restaurants.sort(key=lambda x: (x[0], -x[1]))
    for restaurant in restaurants:
        print(restaurant[2])

=======
Suggestion 8

def main():
    N = int(input())
    # N 個のレストランの情報を格納するリスト
    rest_list = []
    for i in range(N):
        # S_i 市にあり、あなたは 100 点満点中 P_i 点と評価しています。
        S_i, P_i = input().split()
        rest_list.append([i+1, S_i, int(P_i)])

    # 1.市名が辞書順で早いものから紹介していく。
    # 2.同じ市に複数レストランがある場合は、点数が高いものから紹介していく。
    rest_list.sort(key=lambda x: (x[1], -x[2]))

    # N 行出力せよ。i 行目 (1 ≤ i ≤ N) には、i 番目に紹介されるレストランの番号を出力せよ。
    for rest in rest_list:
        print(rest[0])

=======
Suggestion 9

def main():
    N = int(input())
    # リストの要素は、(市名, 点数, レストラン番号)のタプル
    R = []
    for i in range(N):
        S, P = input().split()
        P = int(P)
        R.append((S, P, i+1))
    # 市名で昇順にソート
    R.sort()
    # 同じ市名のレストランの点数で降順にソート
    R = sorted(R, key=lambda x: (x[0], -x[1]))
    for r in R:
        print(r[2])
