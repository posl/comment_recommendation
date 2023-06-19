def main():
    N,M,X,T,D = map(int, input().split())
    height = T
    for i in range(1, N):
        if i == M:
            break
        if i >= X:
            height += D
    print(height)

if __name__ == '__main__':
    main()