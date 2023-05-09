def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A.sort(reverse=True)
    B.sort()
    if A[0] > B[0]:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()