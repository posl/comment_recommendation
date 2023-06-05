def solve():
    N = int(input())
    S = input()
    result = []
    for i in range(1, N):
        l = 0
        while i + l < N:
            if S[l] != S[i + l]:
                l += 1
            else:
                break
        result.append(l)
    for i in result:
        print(i)

if __name__ == '__main__':
    solve()