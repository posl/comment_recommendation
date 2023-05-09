def main():
    Q = int(input())
    operations = []
    for i in range(Q):
        operations.append(list(map(int, input().split())))
    balls = []
    for i in range(Q):
        if operations[i][0] == 1:
            balls.append(operations[i][1])
        elif operations[i][0] == 2:
            balls = [x + operations[i][1] for x in balls]
        else:
            print(min(balls))
            balls.remove(min(balls))
