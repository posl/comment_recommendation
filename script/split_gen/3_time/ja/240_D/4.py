def main():
    N = int(input())
    A = list(map(int, input().split()))
    # 筒に入っているボールの個数
    ball = 0
    # 筒に入っているボールの個数が変わる時間
    time = 0
    # 筒に入っているボールの個数が変わる時間とその個数を格納するリスト
    timeball = [[0, 0]]
    for i in range(N):
        if A[i] == timeball[time][0]:
            timeball[time][1] += 1
        else:
            time += 1
            timeball.append([A[i], 1])
    # 筒に入っているボールの個数が変わる時間とその個数を格納するリストの長さ
    t = len(timeball)
    # 筒に入っているボールの個数が変わる時間とその個数を格納するリストのインデックス
    index = 0
    for i in range(N):
        while index < t - 1 and i >= timeball[index + 1][1]:
            index += 1
        if index % 2 == 0:
            print(ball + timeball[index][1])
        else:
            print(ball)
