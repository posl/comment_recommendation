def main():
    A = list(map(int, input().split()))
    A.sort()
    print("Yes" if A[1] - A[0] == A[2] - A[1] else "No")

if __name__ == '__main__':
    main()