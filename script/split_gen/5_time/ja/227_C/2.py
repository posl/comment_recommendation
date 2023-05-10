def solve():
    N = int(input())
    cnt = 0
    for a in range(1,N+1):
        for b in range(a,N+1):
            if a*b >= N:
                break
            for c in range(b,N+1):
                if a*b*c > N:
                    break
                cnt += 1
    print(cnt)
