def main():
    Q = int(input())
    balls = []
    for i in range(Q):
        line = input()
        line = line.split(" ")
        p = int(line[0])
        if p == 1:
            x = int(line[1])
            balls.append(x)
        elif p == 2:
            x = int(line[1])
            for j in range(len(balls)):
                balls[j] += x
        else:
            balls.sort()
            print(balls.pop(0))
