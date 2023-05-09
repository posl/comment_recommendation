def solve():
    K = int(input())
    ans = []
    for i in range(1, 60):
        for j in range(2**i):
            s = bin(j)[2:]
            s = "0" * (i - len(s)) + s
            s = s.replace("0", "2")
            ans.append(int(s))
    ans.sort()
    print(ans[K - 1])
solve()

if __name__ == '__main__':
    solve()