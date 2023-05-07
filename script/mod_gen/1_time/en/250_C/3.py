def main():
    N, Q = map(int, input().split())
    balls = [i for i in range(1, N+1)]
    for q in range(Q):
        x = int(input())
        index = balls.index(x)
        if index == len(balls)-1:
            balls[index] = balls[0]
            balls[0] = x
        else:
            balls[index] = balls[index+1]
            balls[index+1] = x
    print(*balls)

if __name__ == '__main__':
    main()