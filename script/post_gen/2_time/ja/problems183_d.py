Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, W = map(int, input().split())
    events = []
    for _ in range(N):
        S, T, P = map(int, input().split())
        events.append((S, P))
        events.append((T, -P))
    events.sort()
    now = 0
    for _, P in events:
        now += P
        if now > W:
            print('No')
            return
    print('Yes')

=======
Suggestion 2

def main():
    N, W = map(int, input().split())
    S = [0] * N
    T = [0] * N
    P = [0] * N
    for i in range(N):
        S[i], T[i], P[i] = map(int, input().split())
    # print(S)
    # print(T)
    # print(P)
    # print(N, W)
    # print(S)
    # print(T)
    # print(P)

    # 1分間の状況を配列に格納する
    # 1分間に使われた量の合計がWを超えるか確認する
    # 1分間に使われた量の合計がWを超えたらNoを返す
    # 1分間に使われた量の合計がWを超えなかったらYesを返す
    # 1分間の状況を配列に格納する
    # 1分間に使われた量の合計がWを超えるか確認する
    # 1分間に使われた量の合計がWを超えたらNoを返す
    # 1分間に使われた量の合計がWを超えなかったらYesを返す
    # 1分間の状況を配列に格納する
    # 1分間に使われた量の合計がWを超えるか確認する
    # 1分間に使われた量の合計がWを超えたらNoを返す
    # 1分間に使われた量の合計がWを超えなかったらYesを返す
    # 1分間の状況を配列に格納する
    # 1分間に使われた量の合計がWを超えるか確認する
    # 1分間に使われた量の合計がWを超えたらNoを返す

=======
Suggestion 3

def main():
    N, W = map(int, input().split())
    S = [0] * N
    T = [0] * N
    P = [0] * N
    for i in range(N):
        S[i], T[i], P[i] = map(int, input().split())
    water = [0] * (10**6 + 1)
    for i in range(N):
        water[S[i]] += P[i]
        water[T[i]] -= P[i]
    for i in range(1, 10**6 + 1):
        water[i] += water[i - 1]
    for i in range(10**6 + 1):
        if water[i] > W:
            print("No")
            return
    print("Yes")
    return

=======
Suggestion 4

def main():
    N, W = map(int, input().split())
    water = [0] * 200001
    for _ in range(N):
        S, T, P = map(int, input().split())
        water[S] += P
        water[T] -= P
    for i in range(200000):
        water[i + 1] += water[i]
    for i in range(200000):
        if water[i] > W:
            print('No')
            exit()
    print('Yes')

=======
Suggestion 5

def main():
    N, W = map(int, input().split())
    water = [0] * (2 * 10 ** 5 + 1)
    for i in range(N):
        S, T, P = map(int, input().split())
        water[S] += P
        water[T] -= P
    for i in range(2 * 10 ** 5):
        water[i + 1] += water[i]
    print("Yes" if max(water) <= W else "No")

=======
Suggestion 6

def main():
    N, W = map(int, input().split())
    T = [0] * (2 * 10 ** 5 + 1)
    for i in range(N):
        s, t, p = map(int, input().split())
        T[s] += p
        T[t] -= p
    for i in range(1, 2 * 10 ** 5 + 1):
        T[i] += T[i - 1]
        if T[i] > W:
            print("No")
            exit()
    print("Yes")

=======
Suggestion 7

def main():
    N, W = map(int, input().split())
    P = [list(map(int, input().split())) for _ in range(N)]
    P.sort()
    count = 0
    for i in range(N):
        count += P[i][2]
        if P[i][1] != P[i+1][0]:
            count = 0
        if count > W:
            print('No')
            return
    print('Yes')

=======
Suggestion 8

def main():
    #入力
    N, W = map(int, input().split())
    #N個の人の情報をリストに格納
    people = []
    for i in range(N):
        people.append(list(map(int, input().split())))
    #時刻のリストを作成
    time = []
    for i in range(N):
        time.append(people[i][0])
        time.append(people[i][1])
    time = list(set(time))
    time.sort()
    #各時刻における湯の使用量を計算
    water = [0] * len(time)
    for i in range(N):
        for j in range(len(time)):
            if people[i][0] <= time[j] and time[j] < people[i][1]:
                water[j] += people[i][2]
    #湯の使用量の最大値がWを超えるか判定
    if max(water) > W:
        print('No')
    else:
        print('Yes')

=======
Suggestion 9

def main():
    N, W = map(int, input().split()) #N:人数, W:湯沸かし器の出力
    #S_i:人iが湯沸かし器を使い始める時刻, T_i:人iが湯沸かし器を使い終わる時刻, P_i:人iが1分あたりに使う湯量
    S = [0]*N
    T = [0]*N
    P = [0]*N
    for i in range(N):
        S[i], T[i], P[i] = map(int, input().split())
    
    #1分あたりの湯の使用量を計算
    use = [0]*(2*10**5+1)
    for i in range(N):
        use[S[i]] += P[i]
        use[T[i]] -= P[i]
    
    #累積和を計算
    for i in range(1, 2*10**5+1):
        use[i] += use[i-1]
    
    #湯沸かし器の出力と使用量を比較
    for i in range(2*10**5+1):
        if use[i] > W:
            print("No")
            return
    
    print("Yes")
    return

=======
Suggestion 10

def main():
    N, W = map(int, input().split())
    # お湯を使う人の時間帯を管理するリスト
    time = []
    for _ in range(N):
        S, T, P = map(int, input().split())
        time.append((S, P))
        time.append((T, -P))
    # 時間帯を時刻順にソート
    time.sort()
    # お湯を使う人の時間帯を管理するリスト
    now = 0
    for _, P in time:
        now += P
        if now > W:
            print("No")
            return
    print("Yes")
    return
