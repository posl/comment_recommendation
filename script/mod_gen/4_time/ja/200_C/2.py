def main():
    N = int(input())
    A = list(map(int, input().split()))
    mod = [0] * 200
    for i in range(N):
        mod[A[i] % 200] += 1
    ans = 0
    for i in range(200):
        ans += mod[i] * (mod[i] - 1) // 2
    print(ans)

if __name__ == '__main__':
    main()