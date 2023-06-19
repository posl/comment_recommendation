def main():
    N = int(input())
    A = list(map(int, input().split()))
    min1 = min(A)
    min2 = min(filter(lambda x: x != min1, A))
    for i in range(N):
        if A[i] == min2:
            print(i + 1)
            break

if __name__ == '__main__':
    main()