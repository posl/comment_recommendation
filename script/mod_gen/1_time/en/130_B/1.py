def main():
    N, X = map(int, input().split())
    L = list(map(int, input().split()))
    D = [0]
    for i in range(N):
        D.append(D[i] + L[i])
    print(len([d for d in D if d <= X]))

if __name__ == '__main__':
    main()