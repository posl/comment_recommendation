def main():
    S = input()
    K = int(input())
    S = S.replace('.', ' ')
    S = S.split()
    ans = 0
    for i in range(len(S)):
        ans += len(S[i])
    ans -= K
    ans = max(ans, 0)
    print(ans)

if __name__ == '__main__':
    main()