def main():
    N = int(input())
    A = [list(map(int, input().split())) for _ in range(N)]
    for cx in range(101):
        for cy in range(101):
            for h in range(1000):
                if all([max(h-abs(x-cx)-abs(y-cy),0) == z for x,y,z in A]):
                    print(cx, cy, h)
                    return

if __name__ == '__main__':
    main()