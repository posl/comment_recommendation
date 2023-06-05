def func():
    N = int(input())
    A = list(map(int, input().split()))
    # print(A)
    # print(len(A))
    count = 0
    for i in range(N):
        for j in range(i+1, N):
            if (A[i] - A[j]) % 200 == 0:
                count += 1
    print(count)

if __name__ == '__main__':
    func()