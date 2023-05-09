def problem179b():
    n = int(input())
    d = [list(map(int, input().split())) for _ in range(n)]
    cnt = 0
    for i in range(n-2):
        if d[i][0] == d[i][1] and d[i+1][0] == d[i+1][1] and d[i+2][0] == d[i+2][1]:
            cnt += 1
    if cnt > 0:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    problem179b()