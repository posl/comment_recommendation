def main():
    N = int(input())
    A = list(map(int, input().split()))
    #print(N, A)
    maxA = max(A)
    #print(maxA)
    count = [0] * (maxA+1)
    for i in range(N):
        count[A[i]] += 1
    #print(count)
    ans = 0
    for i in range(1, maxA+1):
        if count[i] % 2 == 1:
            ans += 1
    print((ans+1)//2)

if __name__ == '__main__':
    main()