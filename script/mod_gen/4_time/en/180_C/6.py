def solve(N):
    i = 1
    ans = []
    while i * i <= N:
        if N % i == 0:
            ans.append(i)
            if i != N // i:
                ans.append(N // i)
        i += 1
    ans.sort()
    return ans
N = int(input())
for i in solve(N):
    print(i)

if __name__ == '__main__':
    solve()