def main():
    N = int(input())
    AB = []
    for i in range(N):
        AB.append(list(map(int, input().split())))
    AB.sort(key=lambda x: x[0]+x[1], reverse=True)
    aoki = sum([i[0] for i in AB])
    takahashi = 0
    ans = 0
    for i in range(N):
        aoki -= AB[i][0]
        takahashi += AB[i][0] + AB[i][1]
        ans += 1
        if aoki < takahashi:
            break
    print(ans)

if __name__ == '__main__':
    main()