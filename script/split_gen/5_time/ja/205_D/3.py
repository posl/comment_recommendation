def main():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    K = [int(input()) for _ in range(Q)]
    #A = sorted(A)
    #print(A)
    #print(K)
    for k in K:
        cnt = 0
        for a in A:
            if a <= k:
                cnt += 1
            else:
                break
        print(k+cnt)
