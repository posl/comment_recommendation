def main():
    S = input()
    K = int(input())
    N = len(S)
    i = 0
    ans = 0
    while i < N:
        if S[i] == 'X':
            i += 1
            continue
        j = i
        while j < N and S[j] == '.':
            j += 1
        ans = max(ans, j - i)
        i = j
    print(min(N, ans + 2 * K))

if __name__ == '__main__':
    main()