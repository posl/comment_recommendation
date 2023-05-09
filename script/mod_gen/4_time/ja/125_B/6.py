def main():
    N = int(input())
    V = list(map(int, input().split()))
    C = list(map(int, input().split()))
    max = 0
    for i in range(N):
        if V[i] - C[i] > 0:
            max += V[i] - C[i]
    print(max)

if __name__ == '__main__':
    main()