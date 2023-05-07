def main():
    N, C = map(int, input().split())
    ABC = [list(map(int, input().split())) for _ in range(N)]
    # すぬけプライムに加入する日、脱退する日を取得
    day = []
    for a, b, c in ABC:
        day.append((a, c))
        day.append((b + 1, -c))
    day.sort()
    # すぬけプライムに加入している日数を取得
    sum = 0
    cnt = 0
    for i in range(len(day) - 1):
        sum += day[i][1]
        cnt += min(C, sum) * (day[i + 1][0] - day[i][0])
    print(cnt)
