def main():
    N = int(input())
    W = []
    for i in range(N):
        W.append(input())
    print(W)
    print("Yes" if len(W) == len(set(W)) and all(W[i][0] == W[i-1][-1] for i in range(1, N)) else "No")

if __name__ == '__main__':
    main()