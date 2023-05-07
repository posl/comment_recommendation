def main():
    import math
    N, D = map(int, input().split())
    cnt = 0
    for i in range(N):
        x, y = map(int, input().split())
        if math.sqrt(x**2 + y**2) <= D:
            cnt += 1
    print(cnt)

if __name__ == '__main__':
    main()