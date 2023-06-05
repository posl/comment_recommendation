def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    ans = 0
    for x in range(1, 1001):
        ok = True
        for i in range(N):
            if x < A[i] or x > B[i]:
                ok = False
        if ok:
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()