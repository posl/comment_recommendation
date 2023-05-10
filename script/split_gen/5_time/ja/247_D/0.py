def main():
    Q = int(input())
    query = [list(map(int,input().split())) for _ in range(Q)]
    ball = []
    for i in range(Q):
        if query[i][0] == 1:
            ball += [query[i][1]] * query[i][2]
        else:
            print(sum(ball[:query[i][1]]))
            ball = ball[query[i][1]:]
