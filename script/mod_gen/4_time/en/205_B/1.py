def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    for i in range(1, N+1):
        if A[i-1] != i:
            print("No")
            return
    print("Yes")

if __name__ == '__main__':
    main()