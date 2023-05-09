def main():
    N, Q = map(int, input().split())
    S = input()
    s = [0] * (N+1)
    for i in range(N):
        s[i+1] = s[i] + (S[i:i+2] == 'AC')
    for _ in range(Q):
        l, r = map(int, input().split())
        print(s[r-1] - s[l-1])

if __name__ == '__main__':
    main()