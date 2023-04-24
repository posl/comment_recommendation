Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, W = map(int, input().split())
    S = []
    T = []
    P = []
    for i in range(N):
        s, t, p = map(int, input().split())
        S.append(s)
        T.append(t)
        P.append(p)
    #print(S, T, P)
    ans = "Yes"
    # 0~200000における人数をカウントする
    people = [0] * 200001
    for i in range(N):
        people[S[i]] += P[i]
        people[T[i]] -= P[i]
    #print(people)
    # 累積和を取る
    for i in range(200000):
        people[i+1] += people[i]
    #print(people)
    # 0~200000における人数がWを超えているか判定する
    for i in range(200001):
        if people[i] > W:
            ans = "No"
            break
    print(ans)

=======
Suggestion 2

def main():
    N, W = map(int, input().split())
    event = []
    for _ in range(N):
        S, T, P = map(int, input().split())
        event.append((S, P))
        event.append((T, -P))
    event.sort(key=lambda x: x[0])
    now = 0
    for _, P in event:
        now += P
        if now > W:
            print("No")
            return
    print("Yes")

=======
Suggestion 3

def main():
    N,W=map(int,input().split())
    S=[0]*N
    T=[0]*N
    P=[0]*N
    for i in range(N):
        S[i],T[i],P[i]=map(int,input().split())
    S_max=max(S)
    T_max=max(T)
    #print(S_max,T_max)
    #print(S)
    #print(T)
    #print(P)
    #print(sum(P))
    if sum(P)>W:
        print("No")
        return
    else:
        for i in range(S_max,T_max):
            tmp=0
            for j in range(N):
                if S[j]<=i and i<T[j]:
                    tmp+=P[j]
            if tmp>W:
                print("No")
                return
        print("Yes")

=======
Suggestion 4

def main():
    N, W = map(int, input().split())
    time = [0] * 200001
    for _ in range(N):
        S, T, P = map(int, input().split())
        time[S] += P
        time[T] -= P
    for i in range(200000):
        time[i + 1] += time[i]
        if time[i] > W:
            print("No")
            break
    else:
        print("Yes")

=======
Suggestion 5

def solve():
    N,W = map(int,input().split())
    S = [0]*N
    T = [0]*N
    P = [0]*N
    for i in range(N):
        S[i],T[i],P[i] = map(int,input().split())
    #print(S,T,P)

    #時刻ごとに、その時刻にお湯を使う人の数をカウント
    #時刻 0 から 2×10^5 まで
    count = [0]*(2*10**5+1)
    for i in range(N):
        count[S[i]] += P[i]
        count[T[i]] -= P[i]
    #print(count)

    #時刻ごとに、その時刻にお湯を使う人の数を累積和
    for i in range(1,len(count)):
        count[i] += count[i-1]
    #print(count)

    #時刻ごとに、その時刻にお湯を使う人の数が、給湯器の容量を超えているかチェック
    for i in range(len(count)):
        if count[i] > W:
            print("No")
            return

    print("Yes")

=======
Suggestion 6

def main():
    N,W = map(int,input().split())
    water = [0] * (2*10**5+1)
    for i in range(N):
        S,T,P = map(int,input().split())
        water[S] += P
        water[T] -= P
    for i in range(1,2*10**5+1):
        water[i] += water[i-1]
    if max(water) > W:
        print("No")
    else:
        print("Yes")

=======
Suggestion 7

def main():
    N, W = map(int, input().split())
    # 時刻ごとにお湯を使う量を記録する
    water = [0] * 200001
    for _ in range(N):
        S, T, P = map(int, input().split())
        water[S] += P
        water[T] -= P
    # 時刻ごとにお湯を使う量を累積和で求める
    for i in range(1, 200001):
        water[i] += water[i - 1]
    # 時刻ごとにお湯を使う量が給湯器の出力量を超えていたらNo
    for i in range(200001):
        if water[i] > W:
            print("No")
            return
    print("Yes")

=======
Suggestion 8

def main():
    N, W = map(int, input().split())
    # お湯を使う時刻と、その時刻に使う量をリストに格納
    use = []
    for i in range(N):
        S, T, P = map(int, input().split())
        use.append([S, P])
        use.append([T, -P])
    # 使う量を時刻順に並び替え
    use.sort()
    # お湯の総量
    total = 0
    # お湯の総量が給湯器の量より多くなった場合、Noを出力
    for i in range(len(use)):
        total += use[i][1]
        if total > W:
            print("No")
            return
    print("Yes")

=======
Suggestion 9

def main():
    N, W = map(int, input().split())
    # 2次元配列を作成
    # 0:時刻, 1:人数, 2:リットル数
    water = [[0 for i in range(3)] for j in range(N)]
    for i in range(N):
        S, T, P = map(int, input().split())
        water[i][0] = S
        water[i][1] = 1
        water[i][2] = P
        water.append([T, -1, -P])
    water.sort()
    # print(water)
    # print(water[0][0])
    # print(water[0][1])
    # print(water[0][2])
    # print(water[1][0])
    # print(water[1][1])
    # print(water[1][2])
    # print(water[2][0])
    # print(water[2][1])
    # print(water[2][2])
    # print(water[3][0])
    # print(water[3][1])
    # print(water[3][2])
    # print(water[4][0])
    # print(water[4][1])
    # print(water[4][2])
    # print(water[5][0])
    # print(water[5][1])
    # print(water[5][2])
    # print(water[6][0])
    # print(water[6][1])
    # print(water[6][2])
    # print(water[7][0])
    # print(water[7][1])
    # print(water[7][2])
    # print(water[8][0])
    # print(water[8][1])
    # print(water[8][2])
    # print(water[9][0])
    # print(water[9][1])
    # print(water[9][2])
    # print(water[10][0])
    # print(water[10][1])
    # print(water[10][2])
    # print(water[11][0])
    # print(water[11][1])
    # print(water[11][2])
    #

=======
Suggestion 10

def main():
    N, W = map(int, input().split())
    # 人数, 毎分のリットル数
    # お湯を使う人の数を記録する
    water = [0] * 200001
    for i in range(N):
        S, T, P = map(int, input().split())
        # 時刻, 時刻, 毎分のリットル数
        # 時刻の区間内にお湯を使う人がいることを記録する
        water[S] += P
        water[T] -= P
    # お湯を使う人がいる区間の数を記録する
    water_sum = [0] * 200001
    water_sum[0] = water[0]
    for i in range(1, 200001):
        water_sum[i] = water_sum[i - 1] + water[i]
    for i in range(200001):
        if water_sum[i] > W:
            # お湯を使う人がいる区間の数が毎分のリットル数を超えたら
            # No
            print("No")
            return
    # Yes
    print("Yes")
