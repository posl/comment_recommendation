def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    ans = N
    count = 1
    for i in range(N-1):
        if A[i] == A[i+1]:
            count += 1
        else:
            ans -= count % 2
            count = 1
    ans -= count % 2
    print(ans)

if __name__ == '__main__':
    main()