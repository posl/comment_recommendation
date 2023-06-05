def main():
    N, X = map(int,input().split())
    L = list(map(int,input().split()))
    D = [0]
    for i in range(N):
        D.append(D[i] + L[i])
    for i in range(N+1):
        if D[i] > X:
            print(i)
            break
    else:
        print(N+1)

if __name__ == '__main__':
    main()