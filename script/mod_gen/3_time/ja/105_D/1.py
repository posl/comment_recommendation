def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    ans = 0
    mod = [0] * M
    mod[0] = 1
    s = 0
    for i in range(N):
        s = (s + A[i]) % M
        ans += mod[s]
        mod[s] += 1
    print(ans)

if __name__ == '__main__':
    main()