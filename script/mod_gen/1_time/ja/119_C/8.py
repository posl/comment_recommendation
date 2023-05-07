def main():
    N,A,B,C = map(int,input().split())
    l = [int(input()) for _ in range(N)]
    ans = 10**9
    for i in range(4**N):
        a,b,c = 0,0,0
        mp = 0
        for j in range(N):
            if (i >> (2*j)) & 3 == 1:
                a += l[j]
                mp += 10
            elif (i >> (2*j)) & 3 == 2:
                b += l[j]
                mp += 10
            elif (i >> (2*j)) & 3 == 3:
                c += l[j]
                mp += 10
        if a == 0 or b == 0 or c == 0:
            continue
        mp += abs(A-a) + abs(B-b) + abs(C-c)
        ans = min(ans,mp)
    print(ans)

if __name__ == '__main__':
    main()