def main():
    n = int(input())
    p = list(map(int, input().split()))
    q = list(map(int, input().split()))
    def permutation(n, p):
        ans = 0
        for i in range(n):
            ans *= n - i
            for j in range(i + 1, n):
                if p[i] > p[j]:
                    ans += 1
        return ans
    print(abs(permutation(n, p) - permutation(n, q)))

if __name__ == '__main__':
    main()