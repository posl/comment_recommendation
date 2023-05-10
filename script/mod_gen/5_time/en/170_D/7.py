def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort(reverse=True)
    max_num = A[0]
    count = 0
    for i in range(1, N):
        if max_num % A[i] != 0:
            count += 1
    print(count + 1)

if __name__ == '__main__':
    main()