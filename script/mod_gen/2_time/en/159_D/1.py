def main():
    N = int(input())
    A = list(map(int, input().split()))
    count = [0] * (N+1)
    for a in A:
        count[a] += 1
    ans = [0] * N
    for i in range(1,N+1):
        ans[i-1] = count[i] * (count[i]-1) // 2
    for a in A:
        print(sum(ans) - ans[a-1])

if __name__ == '__main__':
    main()