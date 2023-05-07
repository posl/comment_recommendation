def main():
    N = int(input())
    A = list(map(int, input().split()))
    maxA = max(A)
    count = [0] * (maxA + 1)
    for a in A:
        count[a] += 1
    ans = 0
    for i in range(2, maxA + 1):
        tmp = 0
        for j in range(i, maxA + 1, i):
            tmp += count[j]
        if tmp == 1:
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()