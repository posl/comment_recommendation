def main():
    N = int(input())
    S = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        for a in range(1, 1000):
            for b in range(1, 1000):
                if 4 * a * b + 3 * a + 3 * b == S[i]:
                    break
            else:
                continue
            break
        else:
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()