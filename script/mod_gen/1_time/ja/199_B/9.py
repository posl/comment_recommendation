def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    x = list(range(min(A), max(B) + 1))
    count = 0
    for i in x:
        if all([i >= A[j] and i <= B[j] for j in range(N)]):
            count += 1
    print(count)

if __name__ == '__main__':
    main()