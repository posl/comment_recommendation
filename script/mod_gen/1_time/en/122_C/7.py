def main():
    N, Q = map(int, input().split())
    S = input()
    cumsum = [0]*(N+1)
    for i in range(N-1):
        if S[i:i+2] == "AC":
            cumsum[i+2] = cumsum[i+1] + 1
        else:
            cumsum[i+2] = cumsum[i+1]
    for _ in range(Q):
        l, r = map(int, input().split())
        print(cumsum[r] - cumsum[l])

if __name__ == '__main__':
    main()