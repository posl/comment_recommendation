def main():
    q = int(input())
    balls = []
    for _ in range(q):
        p = list(map(int, input().split()))
        if p[0] == 1:
            balls.append(p[1])
        elif p[0] == 2:
            balls = [x + p[1] for x in balls]
        elif p[0] == 3:
            print(min(balls))
            balls.remove(min(balls))
    return
main()

if __name__ == '__main__':
    main()