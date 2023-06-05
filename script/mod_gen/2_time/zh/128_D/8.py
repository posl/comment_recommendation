def main():
    N, M = list(map(int, input().split()))
    k = []
    s = []
    for i in range(M):
        k.append(list(map(int, input().split()))[0])
        s.append(list(map(int, input().split())))
    p = list(map(int, input().split()))
    # print(N, M)
    # print(k)
    # print(s)
    # print(p)
    # 2**N - 1种可能
    cnt = 0
    for i in range(2**N):
        # print("i = ", i)
        # print("bin(i) = ", bin(i))
        # print("bin(i)[2:] = ", bin(i)[2:])
        # print("len(bin(i)[2:]) = ", len(bin(i)[2:]))
        # print("N - len(bin(i)[2:]) = ", N - len(bin(i)[2:]))
        # print("str(bin(i)[2:]) = ", str(bin(i)[2:]))
        # print("str(bin(i)[2:]).zfill(N) = ", str(bin(i)[2:]).zfill(N))
        # print("str(bin(i)[2:]).zfill(N)[N - len(bin(i)[2:]):] = ", str(bin(i)[2:]).zfill(N)[N - len(bin(i)[2:]):])
        # print("len(str(bin(i)[2:]).zfill(N)[N - len(bin(i)[2:]):]) = ", len(str(bin(i)[2:]).zfill(N)[N - len(bin(i)[2:]):]))
        # print("list(str(bin(i)[2:]).zfill(N)[N - len(bin(i)[2:]):]) = ", list(str(bin(i)[2:]).zfill(N)[N - len(bin(i)[2:]):]))
        # print("list(map(int, str(bin(i)[2:]).zfill(N)[N - len(bin(i)[2:]):])) = ", list(map(int, str(bin(i)[2:]).zfill(N)[N - len(bin(i)[2:]):])))
        # print("list(map(int, str(bin(i)[2:]).zfill(N)[N - len(bin(i)[2:]):])) == [1] * N = ", list(map(int, str(bin(i)[2:]).zfill(N)[N -

if __name__ == '__main__':
    main()