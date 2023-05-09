def solve():
    N = int(input())
    S = input()
    ans = [0]
    for i in range(N):
        if S[i] == 'L':
            ans.insert(0, i+1)
        else:
            ans.append(i+1)
    print(*ans)

if __name__ == '__main__':
    solve()