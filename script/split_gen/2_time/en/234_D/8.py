def main():
    n, k = map(int, input().split())
    p = list(map(int, input().split()))
    p = [0] + p
    psum = [0] * (n + 1)
    for i in range(1, n + 1):
        psum[i] = psum[i - 1] + p[i]
    ans = []
    for i in range(k, n + 1):
        ans.append((psum[i] - psum[i - k]) / k)
    print(*ans, sep='
')
main()
