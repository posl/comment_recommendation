def main():
    Q = int(input())
    query = []
    for i in range(Q):
        query.append([int(i) for i in input().split()])
    ball = []
    for q in query:
        if q[0] == 1:
            ball = ball + [q[1]] * q[2]
        else:
            print(sum(ball[:q[1]]))
            ball = ball[q[1]:]
