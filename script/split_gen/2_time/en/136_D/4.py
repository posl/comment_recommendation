def main():
    S = input()
    N = len(S)
    ans = [0] * N
    count = 0
    for i in range(N):
        if S[i] == 'R':
            count += 1
        else:
            ans[i] += count // 2
            ans[i-1] += (count + 1) // 2
            count = 0
    count = 0
    for i in range(N-1, -1, -1):
        if S[i] == 'L':
            count += 1
        else:
            ans[i] += count // 2
            ans[i+1] += (count + 1) // 2
            count = 0
    print(*ans)
main()
