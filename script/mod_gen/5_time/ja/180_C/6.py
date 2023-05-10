def solve():
    N = int(input())
    ans = set()
    for i in range(1, int(N ** 0.5) + 1):
        if N % i == 0:
            ans.add(i)
            ans.add(N // i)
    for a in sorted(ans):
        print(a)

if __name__ == '__main__':
    solve()