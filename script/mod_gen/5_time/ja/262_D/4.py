def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    A.reverse()
    A.append(0)
    ans = 1
    cnt = 1
    for i in range(0, N):
        if A[i] != A[i+1]:
            ans *= (pow(2, cnt, 998244353) - 1)
            ans %= 998244353
            cnt = 1
        else:
            cnt += 1
    print(ans)

if __name__ == '__main__':
    main()