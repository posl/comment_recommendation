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
