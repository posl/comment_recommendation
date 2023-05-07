def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    A.append(-1)
    ans = 0
    cnt = 1
    for i in range(N):
        if A[i] == A[i+1]:
            cnt += 1
        else:
            ans += cnt * (cnt - 1) // 2
            cnt = 1
    print(ans)

if __name__ == '__main__':
    main()