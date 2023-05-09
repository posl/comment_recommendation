def main():
    N, K = map(int, input().split())
    S = input()
    ans = 0
    for i in range(N):
        if S[i] == '1':
            continue
        if S[i] == '0':
            if i == 0:
                ans = 1
                j = i + 1
                while j < N:
                    if S[j] == '0':
                        ans += 1
                        j += 1
                    else:
                        break
                break
            if S[i - 1] == '0':
                ans = 1
                j = i + 1
                while j < N:
                    if S[j] == '0':
                        ans += 1
                        j += 1
                    else:
                        break
                break
    print(ans)

if __name__ == '__main__':
    main()