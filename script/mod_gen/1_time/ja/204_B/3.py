def main():
    N = int(input())
    A = list(map(int, input().split()))
    answer = 0
    for i in range(N):
        if A[i] > 10:
            answer += A[i] - 10
    print(answer)

if __name__ == '__main__':
    main()