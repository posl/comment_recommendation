Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N = int(input())
    restaurants = []
    for i in range(N):
        S, P = input().split()
        restaurants.append((S, int(P), i+1))
    restaurants.sort(key=lambda x: (x[0], -x[1]))
    for restaurant in restaurants:
        print(restaurant[2])

=======
Suggestion 2

def main():
    N = int(input())
    restaurants = []
    for i in range(N):
        S, P = input().split()
        restaurants.append([i+1, S, int(P)])
    restaurants.sort(key=lambda x: x[2], reverse=True)
    restaurants.sort(key=lambda x: x[1])
    for i in restaurants:
        print(i[0])

=======
Suggestion 3

def main():
    N = int(input())
    restaurants = []
    for i in range(N):
        S, P = input().split()
        restaurants.append((S, int(P), i+1))
    sorted_restaurants = sorted(restaurants, key=lambda x: (x[0], -x[1]))
    for restaurant in sorted_restaurants:
        print(restaurant[2])

=======
Suggestion 4

def main():
    n = int(input())
    restaurant = []
    for i in range(n):
        restaurant.append(input().split())
        restaurant[i][1] = int(restaurant[i][1])
        restaurant[i].append(i+1)

    restaurant.sort(key=lambda x:(x[0],-x[1]))

    for i in range(n):
        print(restaurant[i][2])

=======
Suggestion 5

def main():
    N = int(input())
    restaurant = []
    for i in range(N):
        S, P = input().split()
        restaurant.append((S, int(P), i+1))
    restaurant.sort(key=lambda x: (x[0], -x[1]))
    for i in range(N):
        print(restaurant[i][2])

=======
Suggestion 6

def solve():
    # 入力
    N = int(input())
    S = []
    P = []
    for i in range(N):
        s, p = input().split()
        P.append(int(p))
        S.append(s)

    # 処理
    # 1. 都市名でソート
    # 2. 都市名が同じなら点数でソート
    # 3. 点数が高い順に出力
    # 4. 都市名が同じなら出現順に出力
    # 5. 都市名が異なるなら出現順に出力
    # 6. 1に戻る
    # 7. 終了
    # 1
    sorted_index = sorted(range(N), key=lambda x: S[x])
    # 2
    sorted_index = sorted(sorted_index, key=lambda x: P[x], reverse=True)
    # 3
    sorted_index = sorted(sorted_index, key=lambda x: S[x])
    # 4
    sorted_index = sorted(sorted_index, key=lambda x: S.index(S[x]))
    # 5
    sorted_index = sorted(sorted_index, key=lambda x: S.index(S[x]))
    # 6
    sorted_index = sorted(sorted_index, key=lambda x: S.index(S[x]))
    # 7
    return sorted_index

=======
Suggestion 7

def main():
    N = int(input())
    list = []
    for i in range(N):
        S, P = input().split()
        list.append([S, int(P)])
    list = sorted(list, key=lambda x: (x[0], -x[1]))
    for i in range(N):
        print(list[i][1])

=======
Suggestion 8

def main():
    # N = int(input())
    # S_P = [input().split() for i in range(N)]
    # S_P = sorted(S_P, key=lambda x: x[1], reverse=True)
    # S_P = sorted(S_P, key=lambda x: x[0])
    # for i in range(N):
    #     print(S_P[i][2])

    # N = int(input())
    # S_P = [input().split() for i in range(N)]
    # S_P = sorted(S_P, key=lambda x: x[0])
    # S_P = sorted(S_P, key=lambda x: x[1], reverse=True)
    # for i in range(N):
    #     print(S_P[i][2])

    N = int(input())
    S_P = [input().split() for i in range(N)]
    S_P = sorted(S_P, key=lambda x: x[0])
    S_P = sorted(S_P, key=lambda x: x[1], reverse=True)
    for i in range(N):
        print(S_P[i][2])

=======
Suggestion 9

def sort_list(list):
    list.sort(key=lambda x: x[1], reverse=True)
    return list

N = int(input())
list = []
for i in range(N):
    S, P = input().split()
    P = int(P)
    list.append([S, P, i+1])

list = sort_list(list)
list = sort_list(list)

for i in range(N):
    print(list[i][2])
