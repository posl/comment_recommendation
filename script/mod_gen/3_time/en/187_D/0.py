def main():
    N = int(input())
    AB = []
    for i in range(N):
        AB.append(list(map(int, input().split())))
    AB.sort(key=lambda x: x[0] + x[1], reverse=True)
    Aoki = 0
    Takahashi = 0
    for i in range(N):
        if i % 2 == 0:
            Takahashi += AB[i][0] + AB[i][1]
        else:
            Aoki += AB[i][0]
    if Takahashi > Aoki:
        print(N)
    else:
        for i in range(N):
            Takahashi -= AB[i][0] + AB[i][1]
            Aoki += AB[i][0] + AB[i][1]
            if Takahashi > Aoki:
                print(i + 1)
                break

if __name__ == '__main__':
    main()