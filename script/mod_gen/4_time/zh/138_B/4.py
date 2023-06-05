def main():
    N = int(input())
    A = list(map(int, input().split()))
    sum = 0
    for i in range(N):
        sum += 1/A[i]
    print(1/sum)

if __name__ == '__main__':
    main()