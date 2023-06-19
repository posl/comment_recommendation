def main():
    Q = int(input())
    ball = []
    for i in range(Q):
        query = input().split()
        if query[0] == "1":
            ball.append(int(query[1]))
        elif query[0] == "2":
            for j in range(len(ball)):
                ball[j] += int(query[1])
        elif query[0] == "3":
            print(min(ball))
            ball.remove(min(ball))
