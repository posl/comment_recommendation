def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = [0] * (10 ** 6 + 1)
    for a in A:
        B[a] += 1
    ans = 0
    for i in range(10 ** 6 + 1):
        if B[i] == 0:
            continue
        if B[i] > 1:
            ans += 1
            continue
        j = i + i
        while j <= 10 ** 6:
            B[j] = 0
            j += i
    print(ans)

if __name__ == '__main__':
    main()