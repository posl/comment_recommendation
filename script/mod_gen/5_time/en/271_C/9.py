def problem271_c():
    def solve():
        N = int(input())
        a = list(map(int, input().split()))
        a.sort()
        ans = 0
        for i in range(N):
            if a[i] <= ans + 1:
                ans += a[i]
            else:
                break
        return ans + 1
    print(solve())

if __name__ == '__main__':
    problem271_c()