def main():
    N = int(input())
    S = list(map(int, input().split()))
    count = 0
    for i in range(N):
        a = 1
        b = 1
        while True:
            if 4 * a * b + 3 * a + 3 * b == S[i]:
                break
            else:
                a += 1
                b = 1
                while 4 * a * b + 3 * a + 3 * b < S[i]:
                    b += 1
                    if 4 * a * b + 3 * a + 3 * b == S[i]:
                        break
            if 4 * a * b + 3 * a + 3 * b == S[i]:
                break
            if a >= 1000 and b >= 1000:
                count += 1
                break
    print(count)

if __name__ == '__main__':
    main()