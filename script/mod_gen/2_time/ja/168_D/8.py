def main():
    N, M = map(int, input().split())
    if M != N-1:
        print("No")
        return
    AB = [list(map(int, input().split())) for _ in range(M)]
    AB = [list(map(lambda x: x-1, a)) for a in AB]
    AB.sort()
    ans = [0]*N
    ans[0] = 1
    for i in range(M):
        if ans[AB[i][0]] == 0:
            ans[AB[i][0]] = AB[i][1]+1
        elif ans[AB[i][1]] == 0:
            ans[AB[i][1]] = AB[i][0]+1
        else:
            print("No")
            return
    print("Yes")
    for i in range(N):
        print(ans[i])

if __name__ == '__main__':
    main()