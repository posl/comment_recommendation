def main():
    N = int(input())
    A = list(map(int, input().split()))
    count = 0
    for i in range(N):
        if A[i] == count + 1:
            count += 1
    if count == 0:
        print(-1)
    else:
        print(N - count)

if __name__ == '__main__':
    main()