def main():
    N, M, T = map(int, input().split())
    AB = []
    for i in range(M):
        AB.append(list(map(int, input().split())))
    if N == 0:
        print('No')
        return
    if AB[0][0] > 0:
        print('No')
        return
    now = N
    for i in range(M):
        now -= AB[i][0]
        if now <= 0:
            print('No')
            return
        now += AB[i][1] - AB[i][0]
        if now > N:
            now = N
    now -= T - AB[-1][1]
    if now <= 0:
        print('No')
        return
    print('Yes')
    return

if __name__ == '__main__':
    main()