def main():
    N = int(input())
    W = list(map(int, input().split()))
    S = sum(W)
    s = 0
    for i in range(N):
        s += W[i]
        if s > S/2:
            print(abs(S-s-s+W[i]))
            break
    else:
        print(abs(S-s-s))

if __name__ == '__main__':
    main()