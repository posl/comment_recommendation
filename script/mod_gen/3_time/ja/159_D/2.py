def main():
    N = int(input())
    A = list(map(int, input().split()))
    balls = [0] * N
    for a in A:
        balls[a - 1] += 1
    #print(balls)
    for b in balls:
        if b > 1:
            print(b * (b - 1) // 2)
        else:
            print(0)

if __name__ == '__main__':
    main()