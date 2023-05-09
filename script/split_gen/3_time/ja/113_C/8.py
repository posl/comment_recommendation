def main():
    N, M = map(int, input().split())
    #県ごとに市の数を数える
    pref = [0] * (N+1)
    for i in range(M):
        p, y = map(int, input().split())
        pref[p] += 1
    #県ごとの市の数を累積和にする
    for i in range(1, N+1):
        pref[i] += pref[i-1]
    #市ごとに県と市の番号を出力
    for i in range(M):
        p, y = map(int, input().split())
        print('{:0=6}{:0=6}'.format(p, pref[p-1]+1))
        pref[p-1] -= 1
