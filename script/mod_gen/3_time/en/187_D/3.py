def main():
    N = int(input())
    AB = [list(map(int, input().split())) for _ in range(N)]
    AB.sort(key=lambda x: x[0]+x[1], reverse=True)
    takahashi = 0
    aoki = 0
    for i in range(N):
        aoki += AB[i][0]
    for i in range(N):
        takahashi += AB[i][1]
        aoki -= AB[i][0]
        if takahashi > aoki:
            print(i+1)
            break

if __name__ == '__main__':
    main()