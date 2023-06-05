def main():
    q = int(input())
    balls = []
    for i in range(q):
        p, x = map(int, input().split())
        if p == 1:
            balls.append(x)
        elif p == 2:
            balls = [b + x for b in balls]
        elif p == 3:
            balls.sort()
            print(balls[0])
            balls.pop(0)

if __name__ == '__main__':
    main()