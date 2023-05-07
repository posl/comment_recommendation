def main():
    N, Q = map(int, input().split())
    S = input()
    l = [0] * (N + 1)
    for i in range(N):
        l[i + 1] = l[i]
        if S[i:i + 2] == 'AC':
            l[i + 1] += 1
    for _ in range(Q):
        l_i, r_i = map(int, input().split())
        print(l[r_i - 1] - l[l_i - 1])

if __name__ == '__main__':
    main()