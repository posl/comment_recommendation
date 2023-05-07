def main():
    N = int(input())
    L = list(map(int, input().split()))
    L.sort()
    ans = 0
    for i in range(N - 2):
        a = L[i]
        for j in range(i + 1, N - 1):
            b = L[j]
            for k in range(j + 1, N):
                c = L[k]
                if a != b and b != c and c != a and a + b > c:
                    ans += 1
    print(ans)

if __name__ == '__main__':
    main()