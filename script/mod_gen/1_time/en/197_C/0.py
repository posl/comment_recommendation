def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(30):
        c = 0
        for j in range(N):
            if (A[j] >> i) & 1:
                c += 1
        ans |= ((c % 2) << i)
    print(ans)

if __name__ == '__main__':
    main()