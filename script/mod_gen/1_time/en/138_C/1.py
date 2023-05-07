def main():
    N = int(input())
    V = sorted(list(map(int, input().split())))
    ans = (V[0] + V[1]) / 2
    for i in range(2, N):
        ans = (ans + V[i]) / 2
    print(ans)

if __name__ == '__main__':
    main()