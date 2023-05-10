def main():
    H,N = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    A.reverse()
    if sum(A[0:N-1]) >= H:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()