def main():
    # Input
    N, M = map(int, input().split())
    AB = []
    for i in range(N):
        A, B = map(int, input().split())
        AB.append([A, B])
    # Solve
    AB.sort()
    ans = 0
    day = 0
    for i in range(N):
        if day + AB[i][0] <= M:
            day += AB[i][0]
            ans += AB[i][1]
        else:
            break
    # Output
    print(ans)
main()

if __name__ == '__main__':
    main()