def main():
    # N = int(input())
    # S = list(map(int, input().split()))
    N = 10
    S = [314159265, 358979323, 846264338, -327950288, 419716939, -937510582, 97494459, 230781640, 628620899, -862803482]
    A = [0 for i in range(N)]
    A[0] = S[0]
    for i in range(1, N):
        A[i] = S[i] - A[i-1]
    for i in range(N):
        print(A[i], end=" ")
    print()

if __name__ == '__main__':
    main()