def main():
    N, W = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    ans = 0
    for n in range(1, W+1):
        if n < A[0]:
            continue
        elif n == A[0]:
            ans += 1
        elif n < A[1]:
            ans += 2
        elif n == A[1]:
            ans += 3
        elif n < A[2]:
            ans += 4
        elif n == A[2]:
            ans += 5
        elif n < A[3]:
            ans += 6
        elif n == A[3]:
            ans += 7
        elif n < A[4]:
            ans += 8
        elif n == A[4]:
            ans += 9
        elif n < A[5]:
            ans += 10
        elif n == A[5]:
            ans += 11
        elif n < A[6]:
            ans += 12
        elif n == A[6]:
            ans += 13
        else:
            pass
    print(ans)

if __name__ == '__main__':
    main()