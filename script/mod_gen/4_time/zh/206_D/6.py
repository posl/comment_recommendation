def main():
    N = int(input())
    A = list(map(int, input().split()))
    answer = 0
    for i in range(N//2):
        if A[i] != A[N-1-i]:
            answer += 1
    print(answer)

if __name__ == '__main__':
    main()