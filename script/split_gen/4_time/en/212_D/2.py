def main():
    n = int(input())
    balls = []
    for i in range(n):
        p = input().split()
        if p[0] == "1":
            balls.append(int(p[1]))
        elif p[0] == "2":
            for j in range(len(balls)):
                balls[j] += int(p[1])
        else:
            print(min(balls))
            balls.remove(min(balls))
