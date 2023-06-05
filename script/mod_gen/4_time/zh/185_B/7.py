def main():
    N, M, T = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(M)]
    now = N
    for i in range(M):
        if i == 0:
            now -= AB[i][0]
        else:
            now -= AB[i][0] - AB[i-1][1]
        if now <= 0:
            print("No")
            return
        now += AB[i][1] - AB[i][0]
        if now > N:
            now = N
    now -= T - AB[-1][1]
    if now <= 0:
        print("No")
        return
    print("Yes")

if __name__ == '__main__':
    main()