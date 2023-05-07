def main():
    Q = int(input())
    ball = []
    for i in range(Q):
        query = input().split()
        if query[0] == '1':
            for i in range(int(query[2])):
                ball.append(int(query[1]))
        else:
            for i in range(int(query[1])):
                ball.pop(0)
            print(sum(ball))
            ball = []
