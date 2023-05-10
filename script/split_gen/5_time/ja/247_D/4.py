def main():
    q = int(input())
    ball = []
    for i in range(q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            for j in range(query[2]):
                ball.append(query[1])
        else:
            print(sum(ball[:query[1]]))
            ball = ball[query[1]:]
