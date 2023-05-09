def main():
    N, W = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    ans = 0
    for a in range(N):
        for b in range(N):
            for c in range(N):
                for d in range(N):
                    for e in range(N):
                        for f in range(N):
                            for g in range(N):
                                if A[a] + A[b] + A[c] + A[d] + A[e] + A[f] + A[g] <= W:
                                    ans += 1
    print(ans)
main()

if __name__ == '__main__':
    main()