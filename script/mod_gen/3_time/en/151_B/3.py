def main():
    N, K, M = map(int, input().split())
    A = list(map(int, input().split()))
    goal = N * M
    total = sum(A)
    if total >= goal:
        print(0)
    elif total + K < goal:
        print(-1)
    else:
        print(goal - total)

if __name__ == '__main__':
    main()