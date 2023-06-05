def main():
    N = int(input())
    V = list(map(int, input().split()))
    C = list(map(int, input().split()))
    max_diff = 0
    for i in range(N):
        if V[i] > C[i]:
            max_diff += V[i] - C[i]
    print(max_diff)

if __name__ == '__main__':
    main()