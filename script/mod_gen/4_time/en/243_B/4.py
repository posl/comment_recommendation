def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    count = 0
    for i in range(N):
        if A[i] == B[i]:
            count += 1
    print(count)
    count = 0
    for i in range(N):
        for j in range(N):
            if A[i] == B[j] and i != j:
                count += 1
    print(count)

if __name__ == '__main__':
    main()