def main():
    S = input()
    Q = int(input())
    for _ in range(Q):
        t, k = map(int, input().split())
        while t > 0:
            if k % 2 == 1:
                k = (k + 1) // 2
            else:
                k = (k + 1) // 2 + len(S) // 2
            t -= 1
        print(S[k - 1])

if __name__ == '__main__':
    main()