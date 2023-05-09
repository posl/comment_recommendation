def main():
    N = int(input())
    P = list(map(int, input().split()))
    Q = [0] * N
    for i in range(N):
        Q[P[i] - 1] = i + 1
    ans = []
    for i in range(N):
        ans.append(str(Q[i]))
    print(" ".join(ans))

if __name__ == '__main__':
    main()