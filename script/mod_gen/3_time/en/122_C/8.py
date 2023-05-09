def main():
    N, Q = map(int, input().split())
    S = input()
    l = [0] * N
    for i in range(N-1):
        if S[i] == "A" and S[i+1] == "C":
            l[i+1] = l[i] + 1
        else:
            l[i+1] = l[i]
    for _ in range(Q):
        l_i, r_i = map(int, input().split())
        print(l[r_i-1] - l[l_i-1])

if __name__ == '__main__':
    main()