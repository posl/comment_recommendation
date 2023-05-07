def main():
    n = int(input())
    a = list(map(int, input().split()))
    q = int(input())
    que = [list(map(int, input().split())) for _ in range(q)]
    add = [0] * n
    for i in range(q):
        if que[i][0] == 1:
            add = [que[i][1]] * n
        elif que[i][0] == 2:
            a[que[i][1] - 1] += que[i][2]
        else:
            print(a[que[i][1] - 1] + add[que[i][1] - 1])
