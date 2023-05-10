def main():
    N, X, Y, Z = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    AB = []
    for i in range(N):
        AB.append([i, A[i] + B[i]])
    AB.sort(key=lambda x: x[0])
    AB.sort(key=lambda x: x[1], reverse=True)
    AB = AB[:X+Y+Z]
    AB.sort(key=lambda x: x[0])
    AB.sort(key=lambda x: x[1], reverse=True)
    AB = AB[:X+Y]
    AB.sort(key=lambda x: x[0])
    AB.sort(key=lambda x: x[1], reverse=True)
    AB = AB[:X]
    AB.sort(key=lambda x: x[0])
    AB.sort(key=lambda x: x[1], reverse=True)
    for i in range(X):
        print(AB[i][0] + 1)

if __name__ == '__main__':
    main()