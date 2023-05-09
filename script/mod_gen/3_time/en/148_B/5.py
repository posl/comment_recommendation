def main():
    N = int(input())
    S,T = input().split()
    S = list(S)
    T = list(T)
    ans = []
    for i in range(N):
        ans.append(S[i])
        ans.append(T[i])
    print(''.join(ans))

if __name__ == '__main__':
    main()