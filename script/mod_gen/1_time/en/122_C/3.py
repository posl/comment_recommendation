def main():
    N, Q = map(int, input().split())
    S = input()
    l = [0] * (N + 1)
    for i in range(N):
        l[i + 1] = l[i]
        if S[i] == 'A' and i < N - 1 and S[i + 1] == 'C':
            l[i + 2] = l[i + 1] + 1
        else:
            l[i + 2] = l[i + 1]
    for i in range(Q):
        l_i, r_i = map(int, input().split())
        print(l[r_i] - l[l_i])

if __name__ == '__main__':
    main()