def main():
    N, K = map(int, input().split(' '))
    p = list(map(int, input().split(' ')))
    p = [i+1 for i in p]
    p = [i/2 for i in p]
    ans = sum(p[0:K])
    tmp = ans
    for i in range(N-K):
        tmp = tmp - p[i] + p[i+K]
        if tmp > ans:
            ans = tmp
    print(ans)
