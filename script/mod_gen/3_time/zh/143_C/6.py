def solve():
    N = int(input())
    S = input()
    count = 1
    for i in range(N-1):
        if S[i] != S[i+1]:
            count += 1
    print(count)
    return 0

if __name__ == '__main__':
    solve()