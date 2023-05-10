def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A.sort(reverse=True)
    B.sort(reverse=True)
    for i in range(K):
        if A[i] == B[i]:
            print("Yes")
            return
    print("No")
    return

if __name__ == '__main__':
    main()