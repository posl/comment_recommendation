def main():
    N = int(input())
    A = [int(x) for x in input().split()]
    A.sort()
    if N % 2 == 0:
        ans = 0
        for a in A:
            ans += abs(a)
    else:
        ans = 0
        for a in A:
            ans += abs(a)
        ans -= 2 * abs(A[0])
    print(ans)

if __name__ == '__main__':
    main()