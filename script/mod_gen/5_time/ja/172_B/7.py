def solve():
    S = input()
    T = input()
    ans = len(S)
    for i in range(len(S)):
        count = 0
        for j in range(len(S)):
            if i+j >= len(S):
                if S[i+j-len(S)] != T[j]:
                    count += 1
            else:
                if S[i+j] != T[j]:
                    count += 1
        ans = min(ans, count)
    print(ans)

if __name__ == '__main__':
    solve()