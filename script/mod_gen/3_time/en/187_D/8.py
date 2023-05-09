def main():
    N = int(input())
    AB = [list(map(int, input().split())) for _ in range(N)]
    AB.sort(key = lambda x: x[0] + x[1], reverse=True)
    Aoki = 0
    Takahashi = 0
    for i in range(N):
        Takahashi += AB[i][1]
    for i in range(N):
        Takahashi -= AB[i][1]
        Aoki += AB[i][0]
        if Takahashi < Aoki:
            print(i + 1)
            return

if __name__ == '__main__':
    main()