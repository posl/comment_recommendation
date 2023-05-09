def main():
    #N = int(input())
    #S = [int(i) for i in input().split()]
    N = 10
    S = [314159265, 358979323, 846264338, -327950288, 419716939, -937510582, 97494459, 230781640, 628620899, -862803482]
    A = [0]*N
    for i in range(N):
        A[i] = S[i] - sum(A)
    print(A)

if __name__ == '__main__':
    main()