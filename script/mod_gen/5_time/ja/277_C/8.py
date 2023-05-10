def main():
    N = int(input())
    AB = []
    for _ in range(N):
        AB.append(list(map(int, input().split())))
    AB.sort(key=lambda x: x[1], reverse=True)
    ans = 0
    for i in range(N):
        if ans < AB[i][0]:
            ans = AB[i][0]
    print(ans)

if __name__ == '__main__':
    main()