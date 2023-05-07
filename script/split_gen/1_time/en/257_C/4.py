def main():
    N = int(input())
    S = input()
    W = [int(x) for x in input().split()]
    w = []
    for i in range(N):
        if S[i] == '0':
            w.append(W[i])
    w.sort()
    w.append(10**10)
    ans = 0
    for i in range(N):
        if S[i] == '1':
            ind = bisect.bisect_left(w, W[i])
            if ind > ans:
                ans = ind
    print(ans)
