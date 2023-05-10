def main():
    q = int(input())
    balls = []
    for _ in range(q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            balls.extend([query[1]] * query[2])
        else:
            print(sum(balls[:query[1]]))
            balls = balls[query[1]:]
