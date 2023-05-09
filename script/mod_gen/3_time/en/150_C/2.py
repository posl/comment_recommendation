def main():
    N = int(input())
    P = list(map(int, input().split()))
    Q = list(map(int, input().split()))
    P = [x - 1 for x in P]
    Q = [x - 1 for x in Q]
    ans = abs(P.index(0) - Q.index(0))
    for i in range(1, N):
        ans *= i
        ans += abs(P.index(i) - Q.index(i))
    print(ans)
main()

if __name__ == '__main__':
    main()