def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    if (N-K) % 2 == 0:
        print("Yes")
    else:
        if A[0] != A[K]:
            print("Yes")
        else:
            print("No")

if __name__ == '__main__':
    main()