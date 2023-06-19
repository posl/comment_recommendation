def solve():
    N = int(input())
    a = list(map(int, input().split()))
    ans = []
    for i in range(N, 0, -1):
        if a[i-1] == 1:
            ans.append(i)
            for j in range(1, int(i**0.5)+1):
                if i % j == 0:
                    a[j-1] = 1 - a[j-1]
                    if j != i // j:
                        a[i//j-1] = 1 - a[i//j-1]
    M = sum(a)
    if M == 0:
        print(0)
    else:
        print(M)
        print(*ans[::-1])

if __name__ == '__main__':
    solve()