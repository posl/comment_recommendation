def main():
    N = int(input())
    S = [input() for _ in range(N)]
    T = [1,1]
    for i in range(N):
        if S[i] == "AND":
            T[0] = 2**i - T[1]
            T[1] = 2**(i+1) - T[0]
        else:
            T[0] = 2**i - T[0]
            T[1] = 2**(i+1) - T[0]
    print(T[0])

if __name__ == '__main__':
    main()