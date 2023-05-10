def main():
    q = int(input())
    balls = []
    for i in range(q):
        line = input().split()
        if line[0] == "1":
            balls.append(int(line[1]))
        elif line[0] == "2":
            balls = [x + int(line[1]) for x in balls]
        elif line[0] == "3":
            print(min(balls))
            balls.remove(min(balls))
