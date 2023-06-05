def main():
    S = input()
    Q = int(input())
    t_k = [list(map(int, input().split())) for _ in range(Q)]
    for t, k in t_k:
        t = t % 3
        for _ in range(t):
            S = S.replace('a', 'bc')
            S = S.replace('b', 'ca')
            S = S.replace('c', 'ab')
        print(S[k-1])

if __name__ == '__main__':
    main()