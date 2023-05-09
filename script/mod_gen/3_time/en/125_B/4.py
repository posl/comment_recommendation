def main():
    N = int(input())
    V = [int(v) for v in input().split()]
    C = [int(c) for c in input().split()]
    ans = 0
    for i in range(N):
        ans += max(0, V[i] - C[i])
    print(ans)

if __name__ == '__main__':
    main()