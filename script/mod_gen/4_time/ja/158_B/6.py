def main():
    N, A, B = map(int, input().split())
    blue_balls = N // (A + B) * A
    remain_balls = N % (A + B)
    if remain_balls > A:
        print(blue_balls + A)
    else:
        print(blue_balls + remain_balls)

if __name__ == '__main__':
    main()