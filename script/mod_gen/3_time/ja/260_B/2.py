def main():
    N, X, Y, Z = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    AB = []
    for i in range(N):
        AB.append([i+1, A[i], B[i]])
    AB = sorted(AB, key=lambda x: x[2], reverse=True)
    AB = sorted(AB, key=lambda x: x[1], reverse=True)
    AB = AB[:X+Y+Z]
    AB = sorted(AB, key=lambda x: x[0])
    for i in range(X+Y+Z):
        print(AB[i][0])

if __name__ == '__main__':
    main()