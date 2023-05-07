def main():
    N, K = map(int, input().split())
    A = input().split()
    B = input().split()
    A.sort(reverse=True)
    B.sort(reverse=True)
    if A[0] <= B[0]:
        print("No")
    else:
        print("Yes")

if __name__ == '__main__':
    main()