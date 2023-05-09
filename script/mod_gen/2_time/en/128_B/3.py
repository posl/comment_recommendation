def main():
    N = int(input())
    S = []
    P = []
    for _ in range(N):
        s, p = input().split()
        S.append(s)
        P.append(int(p))
    for i in sorted(range(N), key=lambda i: (-P[i], S[i])):
        print(i + 1)

if __name__ == '__main__':
    main()