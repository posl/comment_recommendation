def main():
    N, X = map(int, input().split())
    P = list(map(int, input().split()))
    for i in range(N):
        if P[i] == X:
            print(i+1)
            break
main()

if __name__ == '__main__':
    main()