def main():
    N = int(input())
    A = input().split()
    sum = 0
    for i in range(N):
        sum += int(A[i])
    print(sum)

if __name__ == '__main__':
    main()