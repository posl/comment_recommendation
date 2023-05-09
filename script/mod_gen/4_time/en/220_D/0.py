def main():
    N = int(input())
    A = list(map(int, input().split()))
    MOD = 998244353
    ans = [0] * 10
    for a in A:
        ans[a] += 1
    for i in range(10):
        for j in range(10):
            ans[(i+j)%10] += ans[i] * ans[j]
    for i in range(10):
        print(ans[i]%MOD)

if __name__ == '__main__':
    main()