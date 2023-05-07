def main():
    N, X = map(int, input().split())
    burger = [1]
    for i in range(N):
        burger = [burger[0]+burger[1]+1] + burger + [burger[0]+burger[1]+1]
    print(burger[N+1] if X == 1 else burger[N+1] if X == burger[0]+burger[1]+1 else min(burger[N+1], max(0, burger[N]-(burger[0]+burger[1]+1-X))))

if __name__ == '__main__':
    main()