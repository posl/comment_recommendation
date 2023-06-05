def main():
    N = int(input())
    tlr = [list(map(int,input().split())) for i in range(N)]
    ans = 0
    for i in range(N):
        for j in range(i+1,N):
            t1,l1,r1 = tlr[i]
            t2,l2,r2 = tlr[j]
            if t1 in [1,2] and t2 in [1,2]:
                if l2 <= r1 and l1 <= r2:
                    ans += 1
            elif t1 in [1,2] and t2 in [3,4]:
                if l2 < r1 and l1 <= r2:
                    ans += 1
            elif t1 in [3,4] and t2 in [1,2]:
                if l2 <= r1 and l1 < r2:
                    ans += 1
            elif t1 in [3,4] and t2 in [3,4]:
                if l2 < r1 and l1 < r2:
                    ans += 1
    print(ans)

if __name__ == '__main__':
    main()