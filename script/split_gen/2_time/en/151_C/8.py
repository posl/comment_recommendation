def main():
    input = sys.stdin.readline
    #N, M = map(int, input().split())
    #A = list(map(int, input().split()))
    #B = list(map(int, input().split()))
    #C = [list(map(int, input().split())) for _ in range(N)]
    N, M = map(int, input().split())
    AC = [0] * N
    WA = [0] * N
    for _ in range(M):
        p, s = input().split()
        p = int(p) - 1
        if AC[p]:
            continue
        if s == 'AC':
            AC[p] = 1
        else:
            WA[p] += 1
    ans1 = sum(AC)
    ans2 = sum(WA[i] for i in range(N) if AC[i])
    print(ans1, ans2)
