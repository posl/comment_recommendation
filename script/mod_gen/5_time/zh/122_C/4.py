def main():
    N, Q = map(int, input().split())
    S = input()
    T = [0] * (N + 1)
    for i in range(1, N):
        if S[i-1] == 'A' and S[i] == 'C':
            T[i+1] = T[i] + 1
        else:
            T[i+1] = T[i]
    for i in range(Q):
        l, r = map(int, input().split())
        print(T[r] - T[l])

if __name__ == '__main__':
    main()