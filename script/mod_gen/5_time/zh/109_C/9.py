def main():
    #N, X = map(int, input().split())
    #x = list(map(int, input().split()))
    N, X = 3, 81
    x = [33, 105, 57]
    #N, X = 1, 1
    #x = [1000000000]
    x.sort()
    if N == 1:
        print(abs(x[0]-X))
        return
    D = abs(x[0]-X)
    for i in range(1, N):
        D = gcd(D, abs(x[i]-X))
    print(D)

if __name__ == '__main__':
    main()