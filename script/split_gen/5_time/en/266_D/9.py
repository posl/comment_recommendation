def main():
    N = int(input())
    snuke = [list(map(int, input().split())) for _ in range(N)]
    # print(snuke)
    time = 0
    snuke_sum = 0
    for i in range(N):
        if snuke[i][0] - time >= abs(snuke[i][1]):
            time = snuke[i][0]
            snuke_sum += snuke[i][2]
        elif snuke[i][0] - time < abs(snuke[i][1]) and snuke[i][1] < 0:
            time = snuke[i][0]
            snuke_sum += snuke[i][2]
        elif snuke[i][0] - time < abs(snuke[i][1]) and snuke[i][1] > 0:
            time = snuke[i][0]
            snuke_sum += snuke[i][2]
        else:
            continue
    print(snuke_sum)
