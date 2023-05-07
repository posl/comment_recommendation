def main():
    #input
    N, M = map(int, input().split())
    AC = [0] * N
    WA = [0] * N
    for _ in range(M):
        p, S = input().split()
        p = int(p) - 1
        if AC[p] == 0:
            if S == 'AC':
                AC[p] = 1
            else:
                WA[p] += 1
    #compute
    ans1 = sum(AC)
    ans2 = 0
    for i in range(N):
        if AC[i] == 1:
            ans2 += WA[i]
    #output
    print(ans1, ans2)

if __name__ == '__main__':
    main()