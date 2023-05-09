def main():
    Q = int(input())
    balls = []
    for i in range(Q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            balls.append([query[1], query[2]])
        elif query[0] == 2:
            takeout = query[1]
            sum = 0
            for i in range(len(balls)):
                sum += balls[i][0] * balls[i][1]
                if sum >= takeout:
                    balls[i][1] -= (sum - takeout) // balls[i][0]
                    if (sum - takeout) % balls[i][0] != 0:
                        balls[i][1] -= 1
                    break
            while balls[0][1] == 0:
                balls.pop(0)
            print(sum)
