def main():
    N = int(input())
    S = list(map(int, input().split()))
    result = 0
    for i in range(N):
        a = 1
        while True:
            b = (S[i] - 3 * a) / (4 * a + 3)
            if b < 1:
                break
            if b.is_integer():
                result += 1
                break
            a += 1
    print(N - result)

if __name__ == '__main__':
    main()