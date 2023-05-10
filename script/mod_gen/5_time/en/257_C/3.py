def main():
    N = int(input())
    S = input()
    W = list(map(int, input().split()))
    max = 0
    for i in range(0, N):
        if S[i] == '0':
            if max < W[i]:
                max = W[i]
    print(max)

if __name__ == '__main__':
    main()