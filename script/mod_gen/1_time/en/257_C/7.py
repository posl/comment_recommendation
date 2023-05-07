def main():
    N = int(input())
    S = input()
    W = list(map(int, input().split()))
    # print(N)
    # print(S)
    # print(W)
    # print("N =", N)
    # print("S =", S)
    # print("W =", W)
    S = S.replace("0", "1")
    S = S.replace("1", "0")
    S = S.replace("0", "1")
    # print("S =", S)
    # print("S =", S)
    w = []
    for i in range(N):
        w.append((W[i], S[i]))
    # p

if __name__ == '__main__':
    main()