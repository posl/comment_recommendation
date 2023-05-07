def main():
    N = int(input())
    V = list(map(int, input().split()))
    C = list(map(int, input().split()))
    answer = 0
    for i in range(N):
        if V[i] > C[i]:
            answer += V[i] - C[i]
    print(answer)

if __name__ == '__main__':
    main()