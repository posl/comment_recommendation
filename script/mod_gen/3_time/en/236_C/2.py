def main():
    N, M = map(int, input().split())
    S = input().split()
    T = input().split()
    ans = []
    for i in range(N):
        if S[i] in T:
            ans.append('Yes')
        else:
            ans.append('No')
    print('
'.join(ans))

if __name__ == '__main__':
    main()