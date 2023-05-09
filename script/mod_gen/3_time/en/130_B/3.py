def main():
    N, X = map(int, input().split())
    L = list(map(int, input().split()))
    D = [0]
    for i in range(1, N+1):
        D.append(D[i-1]+L[i-1])
    print(len([d for d in D if d <= X]))

if __name__ == '__main__':
    main()