def solve():
    N, M, T = map(int, input().split())
    AB = [tuple(map(int, input().split())) for _ in range(M)]
    bat = N
    pre = 0
    for i in range(M):
        bat -= AB[i][0] - pre
        if bat <= 0:
            return False
        bat += AB[i][1] - AB[i][0]
        if bat > N:
            bat = N
        pre = AB[i][1]
    bat -= T - pre
    if bat <= 0:
        return False
    return True

if __name__ == '__main__':
    solve()