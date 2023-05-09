def main():
    N, X = map(int, input().split())
    L = list(map(int, input().split()))
    D = [0]
    for i in range(N):
        D.append(D[-1] + L[i])
    count = 0
    for i in range(N+1):
        if D[i] <= X:
            count += 1
    print(count)

if __name__ == '__main__':
    main()