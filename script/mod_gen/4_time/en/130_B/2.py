def main():
    N, X = map(int, input().split())
    L = list(map(int, input().split()))
    D = 0
    count = 1
    for i in range(N):
        D += L[i]
        if D <= X:
            count += 1
    print(count)

if __name__ == '__main__':
    main()