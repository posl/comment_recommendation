def main():
    #input
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    X = [int(input()) for _ in range(Q)]
    #compute
    A.sort()
    for x in X:
        ans = 0
        for a in A:
            if a >= x:
                break
            ans += 1
        print(N - ans)
