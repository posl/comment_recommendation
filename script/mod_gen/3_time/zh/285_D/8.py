def main():
    N = int(input())
    s = []
    t = []
    for i in range(N):
        S, T = input().split()
        s.append(S)
        t.append(T)
    for i in range(N):
        for j in range(i + 1, N):
            if s[i] == t[j] and s[j] == t[i]:
                print('Yes')
                return
    print('No')

if __name__ == '__main__':
    main()