def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    A.append(0)
    count = 0
    for i in range(N):
        if A[i] != A[i+1]:
            count += 1
        print(count - (N - i - 1))

if __name__ == '__main__':
    main()