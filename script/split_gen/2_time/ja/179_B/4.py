def main():
    N = int(input())
    dice = [input().split() for _ in range(N)]
    cnt = 0
    for i in range(N-2):
        if dice[i][0] == dice[i][1] and dice[i+1][0] == dice[i+1][1] and dice[i+2][0] == dice[i+2][1]:
            cnt += 1
    if cnt > 0:
        print('Yes')
    else:
        print('No')
