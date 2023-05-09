def main():
    N, X = map(int, input().split())
    for c in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
        if X <= N:
            print(c)
            break
        X -= N
main()

if __name__ == '__main__':
    main()