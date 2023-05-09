def main():
    N = int(input())
    A = list(map(int, input().split()))
    generation = [0] * (2*N+1)
    generation[1] = 0
    for i in range(N):
        generation[2*i+2] = generation[A[i]] + 1
        generation[2*i+3] = generation[A[i]] + 1
    for i in range(1, 2*N+1):
        print(generation[i])
main()

if __name__ == '__main__':
    main()