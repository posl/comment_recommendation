def main():
    N = int(input())
    S = input()
    W = list(map(int, input().split()))
    w_c = [0]
    w_a = [0]
    for i in range(N):
        w_c.append(w_c[i])
        w_a.append(w_a[i])
        if S[i] == '0':
            w_c[i+1] += W[i]
        else:
            w_a[i+1] += W[i]
    ans = 0
    for i in range(N+1):
        ans = max(ans, w_c[i]+w_a[N]-w_a[i])
    print(ans)

if __name__ == '__main__':
    main()