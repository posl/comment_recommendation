def main():
    N,K = map(int,input().split())
    A = list(map(int,input().split()))
    ans = 0
    s = 0
    t = 0
    while True:
        if s == N:
            break
        while True:
            if t == N:
                break
            if s == t:
                if A[s] == K:
                    ans += 1
                    t += 1
                    break
                else:
                    t += 1
            else:
                if sum(A[s:t+1]) == K:
                    ans += 1
                    t += 1
                    break
                elif sum(A[s:t+1]) < K:
                    t += 1
                else:
                    break
        s += 1
    print(ans)

if __name__ == '__main__':
    main()