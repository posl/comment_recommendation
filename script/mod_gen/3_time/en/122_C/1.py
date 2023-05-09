def main():
    N, Q = map(int, input().split())
    S = input()
    l = [0] * (N + 1)
    for i in range(1, N):
        if S[i - 1] + S[i] == "AC":
            l[i + 1] = l[i] + 1
        else:
            l[i + 1] = l[i]
    for i in range(Q):
        l_i, r_i = map(int, input().split())
        print(l[r_i] - l[l_i])

if __name__ == '__main__':
    main()