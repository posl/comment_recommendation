def main():
    N, K, M = map(int, input().split())
    A = list(map(int, input().split()))
    goal = N * M
    total = sum(A)
    if total >= goal:
        print(0)
    else:
        required = goal - total
        if required > K:
            print(-1)
        else:
            print(required)

if __name__ == '__main__':
    main()