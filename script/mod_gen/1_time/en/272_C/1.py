def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort(reverse=True)
    even = -1
    for i in range(N-1):
        if A[i] == A[i+1]:
            even = A[i]
            break
    print(even*2)

if __name__ == '__main__':
    main()