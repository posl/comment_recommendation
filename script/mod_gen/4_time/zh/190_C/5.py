def main():
    N,M = map(int,input().split())
    AB = [list(map(int,input().split())) for _ in range(M)]
    K = int(input())
    CD = [list(map(int,input().split())) for _ in range(K)]
    ans = 0
    for i in range(2 ** K):
        S = set()
        for j in range(K):
            if (i >> j) & 1:
                S.add(CD[j][0])
            else:
                S.add(CD[j][1])
        cnt = 0
        for a,b in AB:
            if a in S and b in S:
                cnt += 1
        if ans < cnt:
            ans = cnt
    print(ans)

if __name__ == '__main__':
    main()